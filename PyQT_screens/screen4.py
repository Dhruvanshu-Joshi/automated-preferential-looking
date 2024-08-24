import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSlider, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QPalette, QColor, QBrush, QLinearGradient, QGradient
from PyQt6.QtCore import Qt, pyqtSignal


class SelectHemWindow(QMainWindow):
    navigate_prev = pyqtSignal()
    navigate_next = pyqtSignal(str)

    def __init__(self, panda_image_path, eye_image_path, eye_image_path1, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3):
        super().__init__()
        self.selected_hemisphere = None
        self.selected_hemisphere_button = None
        self.mode = None  # Initialize mode

        # Set up the UI
        self.init_ui(panda_image_path, eye_image_path, eye_image_path1, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3)

    def init_ui(self, panda_image_path, eye_image_path, eye_image_path1, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3):
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(255, 255, 255))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Store the paths to the hover images
        self.hover_images = [hover_image_path1, hover_image_path2, hover_image_path3]
        self.default_image_path = panda_image_path

        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        # Create title label
        self.title_label = QLabel("Select Hemisphere Type", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #008682; padding: 10px; background-color: #EBFFC5;")
        self.title_label.setFixedHeight(200)
        main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Add stretch to push content to the center
        main_layout.addStretch(1)

        # Create the horizontal layout for the buttons
        center_layout = QHBoxLayout()

        # Add stretch to center the content
        center_layout.addStretch(1)

        # Load and set the panda image
        self.panda_label = QLabel(self)
        panda_pixmap = QPixmap(self.default_image_path)
        self.panda_label.setPixmap(panda_pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))
        self.panda_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        center_layout.addWidget(self.panda_label)

        # Create a vertical layout for the buttons
        self.button_layout = QVBoxLayout()
        self.button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        center_layout.addLayout(self.button_layout)

        # Add stretch to center the content
        center_layout.addStretch(1)

        main_layout.addLayout(center_layout)

        # Add stretch to push content to the center
        main_layout.addStretch(1)

        # Create the navigation arrows
        nav_layout = QHBoxLayout()

        self.prev_button = QPushButton("<", self)
        self.prev_button.setStyleSheet("""
            QPushButton {
                font-size: 48px;
                color: #008682;
                background-color: #EBFFC5;
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

        nav_layout.addStretch()

        self.next_button = QPushButton(">", self)
        self.next_button.setStyleSheet("""
            QPushButton {
                font-size: 48px;
                color: #008682;
                background-color: #EBFFC5;
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

        main_layout.addLayout(nav_layout)

        # Connect navigation buttons to signals
        self.prev_button.clicked.connect(self.navigate_prev.emit)
        self.next_button.clicked.connect(self.on_next_button_clicked)

        # Set the central widget of the main window
        self.setCentralWidget(main_widget)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

    def set_mode(self, _, device_type, eye_image_path, eye_image_path1):
        if device_type == 'Eye Tracker':
            self.mode = 'device'
        elif device_type == 'Eye Tracking Model':
            self.mode = 'model'
        else:
            print(device_type)
            print("Unknown device type")
            return

        # Update the UI based on the mode
        self.update_ui_based_on_mode(eye_image_path, eye_image_path1)

    def update_ui_based_on_mode(self, eye_image_path, eye_image_path1):
        # Load the eye images
        eye_pixmap = QPixmap(eye_image_path).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
        eye_pixmap1 = QPixmap(eye_image_path1).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)

        if self.mode == 'device':
            self.create_test_button(self.button_layout, eye_pixmap, "Two Hemispheres", "#EBFFC5;", "#008682", 0)
            self.button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
            self.create_test_button(self.button_layout, eye_pixmap1, "Four Hemispheres", "#EBFFC5;", "#008682", 1)
        elif self.mode == 'model':
            self.create_test_button(self.button_layout, eye_pixmap, "Two Hemispheres", "#EBFFC5;", "#008682", 0)

    def create_test_button(self, layout, icon_pixmap, text, color, txt_color, hover_index):
        button_layout = QHBoxLayout()

        icon_label = QLabel(self)
        icon_label.setPixmap(icon_pixmap)
        icon_label.setFixedSize(60, 60)

        button = QPushButton(text, self)
        button.setStyleSheet(f"""
            QPushButton {{
                font-size: 24px;
                font-weight: bold;
                color: {txt_color};
                background-color: {color};
                padding: 10px 20px;
                border-radius: 20px;
            }}
            QPushButton:hover {{
                background-color: {self.adjust_color_brightness(color, 1.2)};
            }}
            QPushButton:pressed {{
                background-color: {self.adjust_color_brightness(color, 0.8)};
            }}
        """)
        button.setFixedSize(400, 60)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        # Connect button hover events to methods
        button.enterEvent = lambda event, idx=hover_index: self.on_button_hover_enter(idx)
        button.leaveEvent = lambda event, idx=hover_index: self.on_button_hover_leave()

        button.clicked.connect(lambda: self.on_hem_button_click(button, text))

        button_layout.addWidget(icon_label)
        button_layout.addWidget(button)
        button_layout.addStretch()

        layout.addLayout(button_layout)

    def adjust_color_brightness(self, color, factor):
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        r = min(255, max(0, int(r * factor)))
        g = min(255, max(0, int(g * factor)))
        b = min(255, max(0, int(b * factor)))
        return f"#{r:02X}{g:02X}{b:02X}"

    def on_button_hover_enter(self, index):
        hover_pixmap = QPixmap(self.hover_images[index])
        self.panda_label.setPixmap(hover_pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))

    def on_button_hover_leave(self):
        default_pixmap = QPixmap(self.default_image_path)
        self.panda_label.setPixmap(default_pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))

    def on_hem_button_click(self, button, text):
        if self.selected_hemisphere_button:
            self.selected_hemisphere_button.setEnabled(True)  # Enable the previously selected button
            self.selected_hemisphere_button.setStyleSheet(self.selected_hemisphere_button.styleSheet().replace(self.adjust_color_brightness("#EBFFC5", 0.8), "#EBFFC5"))

        button.setEnabled(False)  # Disable the clicked button
        button.setStyleSheet(button.styleSheet().replace("#EBFFC5", self.adjust_color_brightness("#EBFFC5", 0.8)))  # Darken the disabled button
        self.selected_hemisphere_button = button  # Update the selected button
        self.selected_hemisphere = text  # Update the selected test
        print(f"{text} button clicked!")
        self.navigate_next.emit(text)

    def on_next_button_clicked(self):
        if self.mode:
            self.navigate_next.emit(self.mode)
        else:
            print("No mode selected!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

    def get_hemisphere(self):
        # if not self.selected_hem_button:
            # raise ValueError('Please choose button corresponding to the hemispheres')
        return self.selected_hemisphere_button

if __name__ == "__main__":
    app = QApplication([])
    # Paths to the provided images
    panda_image_path = 'panda7.png'
    eye_image_path = 'eye1.png'  # Replace with the correct path to the eye image
    eye_image_path1 = 'eye2.png'
    eye_image_path2 = 'eye3.png'
    hover_image_path1 = 'panda2.png'  # Replace with the correct path to the hover image 1
    hover_image_path2 = 'panda3.png'  # Replace with the correct path to the hover image 2
    hover_image_path3 = 'panda4.png'  # Replace with the correct path to the hover image 3

    window = SelectHemWindow(panda_image_path, eye_image_path, eye_image_path, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3)

    window.set_mode('-','Eye Tracking Model', eye_image_path, eye_image_path1)  # or 'Eye Tracking Model'
    app.exec()
