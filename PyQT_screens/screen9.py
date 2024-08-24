import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon, QPalette, QColor, QBrush, QLinearGradient, QGradient
from PyQt6.QtCore import Qt, pyqtSignal, QSize

class SelectVideoSourceWindow(QMainWindow):
    navigate_prev = pyqtSignal()  # Custom signal for navigation to the previous screen
    navigate_next = pyqtSignal(str)  # Custom signal for navigation to the next screen

    def __init__(self, parent=None):
        super().__init__(parent)

        self.camera_or_file = None

        # Main widget and layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)

        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(208, 244, 229))
        gradient.setColorAt(1.0, QColor(189, 234, 204))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Create title label
        self.title_label = QLabel("Select Video Source", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #008682; padding: 10px; background-color: #EBFFC5;")
        self.title_label.setFixedHeight(100)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Add stretch to push content to the center
        self.main_layout.addStretch(1)

        # Create buttons
        self.create_buttons()

        # Add stretch to push content to the center
        self.main_layout.addStretch(1)

        # Add navigation buttons layout
        self.create_navigation_buttons()

        # Set main widget
        self.setCentralWidget(self.main_widget)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

    def camera_clicked(self):
        self.camera_or_file = 0
        self.camera_button.setStyleSheet(self.get_selected_button_style("#05703c"))
        self.file_button.setStyleSheet(self.get_default_button_style("#0258B2"))

    def get_selected_button_style(self, base_color):
        return f"""
            QPushButton {{
                font-size: 24px;
                font-weight: bold;
                color: white;
                background-color: {self.adjust_color_brightness(base_color, 0.8)};
                padding: 10px 20px;
                border-radius: 30px;
                border: 2px solid white;
            }}
        """
    
    def get_default_button_style(self, base_color):
        return f"""
            QPushButton {{
                font-size: 24px;
                font-weight: bold;
                color: white;
                background-color: {base_color};
                padding: 10px 20px;
                border-radius: 30px;
            }}
            QPushButton:hover {{
                background-color: {self.adjust_color_brightness(base_color, 1.2)};
            }}
            QPushButton:pressed {{
                background-color: {self.adjust_color_brightness(base_color, 0.8)};
            }}
        """

    def create_buttons(self):
        button_layout = QHBoxLayout()

        # Add camera button
        self.camera_button = self.create_button("Camera", "camera_icon.png", "#05703c")
        self.camera_button.clicked.connect(self.camera_clicked)
        button_layout.addWidget(self.camera_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add file button
        self.file_button = self.create_button("File", "file_icon.png", "#0258B2")
        self.file_button.clicked.connect(self.open_file_dialog)
        button_layout.addWidget(self.file_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addLayout(button_layout)

    def create_button(self, text, icon_path, color):
        button = QPushButton(text, self)
        button.setIcon(QIcon(icon_path))
        button.setIconSize(QSize(80, 80))
        button.setFixedSize(300, 150)
        button.setStyleSheet(f"""
            QPushButton {{
                font-size: 24px;
                font-weight: bold;
                color: white;
                background-color: {color};
                padding: 10px 20px;
                border-radius: 30px;
            }}
            QPushButton:hover {{
                background-color: {self.adjust_color_brightness(color, 1.2)};
            }}
            QPushButton:pressed {{
                background-color: {self.adjust_color_brightness(color, 0.8)};
            }}
        """)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        return button

    def adjust_color_brightness(self, color, factor):
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        r = min(255, max(0, int(r * factor)))
        g = min(255, max(0, int(g * factor)))
        b = min(255, max(0, int(b * factor)))
        return f"#{r:02X}{g:02X}{b:02X}"

    def create_navigation_buttons(self):
        nav_layout = QHBoxLayout()

        self.prev_button = QPushButton("<", self)
        self.prev_button.setStyleSheet("""
            QPushButton {
                font-size: 48px;
                color: #008682;
                background-color: #A2F58E;
                border-radius: 40px;
                border: 2px solid #008000;
            }
            QPushButton:hover {
                background-color: #79D877;
            }
            QPushButton:pressed {
                background-color: #5EBB61;
            }
        """)
        self.prev_button.setFixedSize(80, 80)
        self.prev_button.setCursor(Qt.CursorShape.PointingHandCursor)
        nav_layout.addWidget(self.prev_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.prev_button.clicked.connect(self.navigate_prev.emit)

        nav_layout.addStretch()

        self.next_button = QPushButton(">", self)
        self.next_button.setStyleSheet("""
            QPushButton {
                font-size: 48px;
                color: #008682;
                background-color: #A2F58E;
                border-radius: 40px;
                border: 2px solid #008000;
            }
            QPushButton:hover {
                background-color: #79D877;
            }
            QPushButton:pressed {
                background-color: #5EBB61;
            }
        """)
        self.next_button.setFixedSize(80, 80)
        self.next_button.setCursor(Qt.CursorShape.PointingHandCursor)
        nav_layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignRight)
        self.next_button.clicked.connect(self.on_next_button_clicked)

        self.main_layout.addLayout(nav_layout)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mov)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            print(f"Selected files: {selected_files}")
            # You can now process the selected files
            self.camera_or_file = selected_files
            self.file_button.setStyleSheet(self.get_selected_button_style("#0258B2"))
            self.camera_button.setStyleSheet(self.get_default_button_style("#05703c"))

    def on_next_button_clicked(self):
        # Emit the navigation signal with the appropriate information
        if self.camera_or_file==0:
            self.navigate_next.emit("camera")
        elif self.camera_or_file is not None:
            self.navigate_next.emit(self.camera_or_file[0])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

    def get_video_camera(self):
        return self.camera_or_file

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SelectVideoSourceWindow()
    sys.exit(app.exec())
