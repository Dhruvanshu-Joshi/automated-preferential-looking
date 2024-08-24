import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QProgressBar, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer

class progressWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Progress Bar Example')
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
        
        # Add text label to the layout
        self.main_layout.addWidget(self.text_label)
        
        # Load the image
        pixmap = QPixmap('load.png')

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setStyleSheet("background: transparent;")

        # Create a QWidget to contain the image and progress bar
        self.overlay_widget = QWidget(self)
        self.overlay_layout = QVBoxLayout(self.overlay_widget)
        self.overlay_layout.setContentsMargins(0, 0, 0, 0)
        self.overlay_layout.setSpacing(0)
        self.overlay_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add image label to the overlay layout
        self.overlay_layout.addWidget(self.image_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setTextVisible(False)  # Hide the default text
        self.progress_bar.setFixedWidth(pixmap.width()+250)  # Set progress bar width to image width
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

        # Add the progress bar to the overlay layout
        self.overlay_layout.addWidget(self.progress_bar, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add the overlay widget to the main layout
        self.main_layout.addWidget(self.overlay_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Add a spacer to position the progress bar 15 pixels above the bottom of the image
        self.spacer = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.main_layout.addSpacerItem(self.spacer)

        # Start the progress bar loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  # Update every 100 ms

        self.progress_value = 0

    def update_progress(self):
        self.progress_value += 1
        if self.progress_value > 100:
            self.progress_value = 0
        self.progress_bar.setValue(self.progress_value)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = progressWindow()
    window.show()
    sys.exit(app.exec())
