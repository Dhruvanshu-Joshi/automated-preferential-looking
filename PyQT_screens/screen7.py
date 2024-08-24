import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, pyqtSignal, QTimer

class ExpWindow(QMainWindow):
    navigate_next = pyqtSignal()  # Custom signal for navigating to the next screen
    navigate_prev = pyqtSignal()  # Custom signal for navigating to the previous screen

    def __init__(self, overlay_image1_path, overlay_image2_path):
        super().__init__()

        # Create a QLabel to display the image
        self.label = QLabel(self)

        screen_size = QApplication.primaryScreen().size()

        # Create a QWidget for the overlay
        self.overlay = QWidget(self.label)
        self.overlay.setGeometry(0, 0, screen_size.width(), screen_size.height())

        # Set a grey gradient background for the overlay
        self.overlay.setStyleSheet("""
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:0,
                stop:0 rgba(112, 112, 112, 255), 
                stop:1 rgba(255, 255, 255, 255)
            );
        """)

        # Create a QLabel for the text
        self.text_label = QLabel(self.overlay)
        self.text_label.setText("Spatial Frequency: 1.618\nContrast: 0.500")
        self.text_label.setStyleSheet("color: white; font-size: 48px; font-weight: bold; background-color: rgba(0, 0, 0, 0);")
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_label.setFont(QFont('Arial', 48))

        # Set the geometry for the text label
        self.text_label.setGeometry(
            screen_size.width() // 2 - 300,
            screen_size.height() // 2 - 50,
            600,
            100
        )

        # Load and set the overlay images
        self.overlay_image2 = QLabel(self.overlay)
        overlay_pixmap2 = QPixmap(overlay_image2_path)
        self.overlay_image2.setPixmap(overlay_pixmap2.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
        self.overlay_image2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.overlay_image2.setGeometry(screen_size.width() - 600, screen_size.height() - 350, 300, 300)
        
        self.overlay_image1 = QLabel(self.overlay)
        overlay_pixmap1 = QPixmap(overlay_image1_path)
        self.overlay_image1.setPixmap(overlay_pixmap1.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
        self.overlay_image1.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.overlay_image1.setGeometry(screen_size.width() - 350, screen_size.height() - 350, 300, 300)


        # Set the central widget of the main window
        self.setCentralWidget(self.label)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

        # Set up a QTimer to trigger the navigate_next signal after 5 seconds
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.start(5000)
        self.timer.timeout.connect(self.navigate_next.emit)
          # 5000 milliseconds = 5 seconds

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Paths to the overlay images
    overlay_image1_path = 'stimulus.png'  # Replace with your actual overlay image path
    overlay_image2_path = 'panda8.png'  # Replace with your actual overlay image path

    window = ExpWindow(overlay_image1_path, overlay_image2_path)

    # Connect the signals to slots (functions)
    window.navigate_prev.connect(lambda: print("Navigate to previous screen"))
    window.navigate_next.connect(lambda: print("Navigate to next screen"))

    sys.exit(app.exec())
