import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

class startWindow(QMainWindow):
    navigate_next = pyqtSignal()  # Custom signal for navigating to the next screen
    navigate_prev = pyqtSignal()  # Custom signal for navigating to the previous screen

    def __init__(self, image_path):
        super().__init__()

        # Create a QLabel to display the image
        self.label = QLabel(self)

        # Load the image and scale it to the screen size
        pixmap = QPixmap(image_path)
        screen_size = QApplication.primaryScreen().size()
        scaled_pixmap = pixmap.scaled(screen_size, Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        # Set the scaled pixmap to the label
        self.label.setPixmap(scaled_pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create a QWidget for the overlay
        self.overlay = QWidget(self.label)
        self.overlay.setGeometry(0, 0, screen_size.width(), screen_size.height())

        # Create the start button
        self.start_button = QPushButton("Start Experiment", self.overlay)
        self.start_button.setStyleSheet("""
            QPushButton {
                font-size: 24px; font-weight: bold; background-color: #DBFAF6; padding: 10px 20px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #79D877;  /* Darker color on hover */
            }
            QPushButton:pressed {
                background-color: #5EBB61;  /* Darker color on click */
            }
        """)
        self.start_button.setFixedSize(250, 60)
        self.start_button.setGeometry(screen_size.width() // 2 - 45, screen_size.height() // 2 - 60, 250, 60)
        self.start_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.start_button.clicked.connect(self.navigate_next.emit)

        # Create the previous button
        self.prev_button = QPushButton("Previous", self.overlay)
        self.prev_button.setStyleSheet("""
            QPushButton {
                font-size: 24px; font-weight: bold; background-color: #DBFAF6; padding: 10px 20px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #79D877;  /* Darker color on hover */
            }
            QPushButton:pressed {
                background-color: #5EBB61;  /* Darker color on click */
            }
        """)
        self.prev_button.setFixedSize(250, 60)
        self.prev_button.setGeometry(screen_size.width() // 2 - 45, screen_size.height() // 2 + 20, 250, 60)
        self.prev_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.prev_button.clicked.connect(self.navigate_prev.emit)

        # Set the central widget of the main window
        self.setCentralWidget(self.label)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Path to the provided image file
    image_path = 'start.png'  # Replace with your actual image path
    window = startWindow(image_path)

    # Connect the signals to slots (functions)
    window.navigate_prev.connect(lambda: print("Navigate to previous screen"))
    window.navigate_next.connect(lambda: print("Navigate to next screen"))

    sys.exit(app.exec())
