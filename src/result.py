import sys
import os
import numpy as np
from PIL import Image
# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QApplication
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
from predict import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QEventLoop

# Function to process frames
def process_frames(predict_data, predict_frames, levels_or_contrast, output_file_path, opt, feedback, staircase_loop=None, psychometric_func=None, progress_callback=None):
    frames_dir = 'frames'
    os.makedirs(frames_dir, exist_ok=True)

    vid_frames = []  # Initialize vid_frames to store all frames

    total_frames = sum(len(predict_frames) for frames in predict_frames)
    # total_frames = len(predict_frames)
    processed_frames = 0

    with open(output_file_path, 'a') as f:
        for index, (b, frames, level_or_contrast) in enumerate(zip(predict_data, predict_frames, levels_or_contrast)):
            answers, confidences, frames = predict_from_actual_frames(frames)
            vid_frames += frames
            processed_frames += len(frames)

            if answers[np.argmax(confidences)] == b:
                correct = 1  # correct non-response
            else:
                correct = 0

            if psychometric_func:
                psychometric_func.addData('key_resp_2.corr', correct)
            elif staircase_loop:
                staircase_loop.addResponse(correct, level_or_contrast)

            if level_or_contrast in feedback:
                feedback[level_or_contrast].append(correct)
            else:
                feedback[level_or_contrast] = [correct]

            answer = answers[np.argmax(confidences)]
            b_str = "left" if b == 1 else "right" if b == 2 else str(b)

            for i, frame in enumerate(frames):
                img = Image.fromarray(np.uint8(frame))
                img_path = os.path.join(frames_dir, f"frame_{index}_{i}.png")
                img.save(img_path)

            f.write(f"b: {b} ({b_str}), Answer: {answer}\n")
            f.write(f"Details: opt={opt}, level_or_contrast={level_or_contrast}, correct={correct}\n")
            f.write("-----\n")

            # Update progress
            if progress_callback:
                progress = int((processed_frames / total_frames) * 100)
                progress_callback.emit(progress)

    return vid_frames  # Return the accumulated frames

# Worker class to process video frames in a separate thread
class Worker(QThread):
    progressChanged = pyqtSignal(int)
    finished = pyqtSignal(list)  # Emit vid_frames when done

    def __init__(self, predict_data, predict_frames, levels_or_contrast, output_file_path, opt, feedback, staircase_loop=None, psychometric_func=None, parent=None):
        super(Worker, self).__init__(parent)
        self.predict_data = predict_data
        self.predict_frames = predict_frames
        self.levels_or_contrast = levels_or_contrast
        self.output_file_path = output_file_path
        self.opt = opt
        self.feedback = feedback
        self.staircase_loop = staircase_loop
        self.psychometric_func = psychometric_func
        self.vid_frames=[]

    def run(self):
        self.vid_frames = process_frames(self.predict_data, self.predict_frames, self.levels_or_contrast,
                                    self.output_file_path, self.opt, self.feedback,
                                    staircase_loop=self.staircase_loop,
                                    psychometric_func=self.psychometric_func,
                                    progress_callback=self.progressChanged)
        self.finished.emit(self.vid_frames)

# progressWindow class to display the GUI
class progressWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Loading Screen')
        self.showFullScreen()

        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        screen_size = QApplication.primaryScreen().size()
        self.central_widget.setGeometry(0, 0, screen_size.width(), screen_size.height())

        # Set a grey gradient background for the overlay
        self.central_widget.setStyleSheet("""
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(255, 255, 255, 255), 
                stop:1 rgba(255, 255, 255, 255)
            );
        """)

        # Create main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a QLabel for the text
        self.text_label = QLabel('Finalising Result ....', self)
        self.text_label.setStyleSheet("font-size: 20px; font-weight: Bold;")
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.main_layout.addWidget(self.text_label)

        # Load the image
        pixmap = QPixmap('load.png')

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background: transparent;")
        self.main_layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 38)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedWidth(pixmap.width() + 250)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 #00FF00, stop:1 #007F00);
                width: 2.0px;
            }
        """)
        self.main_layout.addWidget(self.progress_bar, alignment=Qt.AlignmentFlag.AlignCenter)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def on_finish(self, vid_frames):
        self.close()
        print("Processing complete!")
        # Proceed with vid_frames, e.g., saving the video

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Show the loading screen
    loading_screen = progressWindow()
    loading_screen.show()

    # # Example data (replace with actual data)
    # predict_data = []  # Your data here
    # predict_frames = []  # Your data here
    # levels_or_contrast = []  # Your data here
    # output_file_path = 'output.txt'
    # opt = 1
    # feedback = {}
    psychometric_func = None  # Replace with your psychometric function object

     # Generate test data with blank frames
    num_frames = 10
    frame_size = (480, 640, 3)  # Example frame size (height, width, channels)
    blank_frame = np.zeros(frame_size, dtype=np.uint8)  # Create a blank frame (black image)

    predict_data = [0] * num_frames  # Dummy data
    predict_frames = [[blank_frame for _ in range(5)] for _ in range(num_frames)]  # List of blank frames
    levels_or_contrast = [0] * num_frames  # Dummy levels or contrast values
    output_file_path = 'output.txt'
    opt = 1
    feedback = {}
    value={}

    # Create a QEventLoop to wait for the worker to finish
    loop = QEventLoop()
    # Create and start the worker thread
    worker = Worker(predict_data, predict_frames, levels_or_contrast,
                    output_file_path, opt, feedback, psychometric_func=psychometric_func)
    worker.progressChanged.connect(loading_screen.update_progress)
    worker.finished.connect(loop.quit)
    worker.finished.connect(loading_screen.on_finish)
    worker.start()

    # sys.exit(app.exec())
    loop.exec_() 

    import matplotlib.pyplot as plt
    plt.plot(value,feedback, marker='o')
    plt.xlabel('contrast')

# naming the y axis
    plt.ylabel('percent correct')
    plt.title('Psychometric function')
   

    plt.show()
    plt.close()