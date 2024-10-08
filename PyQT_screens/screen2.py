import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal

class SelectTestWindow(QMainWindow):
    navigate_prev = pyqtSignal()
    navigate_next = pyqtSignal(str)  # Send the selected test type to the next screen

    def __init__(self, panda_image_path, eye_image_path, eye_image_path1, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3):
        super().__init__()

        # Store the paths to the hover images
        self.hover_images = [hover_image_path1, hover_image_path2, hover_image_path3]
        self.default_image_path = panda_image_path
        self.selected_test = None  # Initialize selected test to None
        self.selected_button = None  # Initialize selected button to None

        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        # Create title label
        self.title_label = QLabel("Select Test", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #008682; padding: 10px; background-color: #EBFFC5;")
        self.title_label.setFixedHeight(200)
        main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Add stretch to push content to the center
        main_layout.addStretch(1)

        # Create the horizontal layout for the buttons and panda image
        center_layout = QHBoxLayout()

        # Add stretch to center the content
        center_layout.addStretch(1)

        # Load and set the panda image
        self.panda_label = QLabel(self)
        panda_pixmap = QPixmap(self.default_image_path)
        self.panda_label.setPixmap(panda_pixmap.scaled(600, 600, Qt.AspectRatioMode.KeepAspectRatio))
        self.panda_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        center_layout.addWidget(self.panda_label)

        # Create a vertical layout for the test buttons
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Load the eye image
        eye_pixmap = QPixmap(eye_image_path).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)

        # Create test buttons with eye images as visual pointers
        self.create_test_button(button_layout, eye_pixmap, "Contrast Sensitivity", "#05703c", "#fefefe", 0)
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        eye_pixmap1 = QPixmap(eye_image_path1).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
        self.create_test_button(button_layout, eye_pixmap1, "Spatial Frequency", "#0258B2", "#DBFAF6", 1)
        eye_pixmap2 = QPixmap(eye_image_path2).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        self.create_test_button(button_layout, eye_pixmap2, "Vernier Acuity", "#760094", "#FBECFF", 2)

        center_layout.addLayout(button_layout)

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

        main_layout.addLayout(nav_layout)

        # Connect navigation buttons to signals
        self.prev_button.clicked.connect(self.navigate_prev.emit)
        self.next_button.clicked.connect(self.on_next_button_clicked)

        # Set the central widget of the main window
        self.setCentralWidget(main_widget)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

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
                color: {"white"};
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
        button.clicked.connect(lambda: self.on_button_click(button, text))  # Connect button click to method

        button_layout.addWidget(icon_label)
        button_layout.addWidget(button)
        button_layout.addStretch()

        layout.addLayout(button_layout)

        if not hasattr(self, 'test_buttons'):
            self.test_buttons = []
        self.test_buttons.append(button)

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

    def on_button_click(self, button, text):
        if self.selected_button:
            self.selected_button.setEnabled(True)  # Enable the previously selected button
            self.selected_button.setStyleSheet(self.selected_button.styleSheet().replace("darkgray", "white"))

        button.setEnabled(False)  # Disable the clicked button
        button.setStyleSheet(button.styleSheet().replace("white", "darkgray"))  # Darken the disabled button
        self.selected_button = button  # Update the selected button
        self.selected_test = text  # Update the selected test
        print(f"{text} button clicked!")
        self.navigate_next.emit(text)

    def get_test(self):
        return self.selected_test

    def on_next_button_clicked(self):
        if self.selected_test:
            self.navigate_next.emit(self.selected_test)
        else:
            print("No test selected!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Paths to the provided images
    panda_image_path = 'panda.png'
    eye_image_path = 'eye1.png'  # Replace with the correct path to the eye image
    eye_image_path1 = 'eye2.png'
    eye_image_path2 = 'eye3.png'
    hover_image_path1 = 'panda2.png'  # Replace with the correct path to the hover image 1
    hover_image_path2 = 'panda3.png'  # Replace with the correct path to the hover image 2
    hover_image_path3 = 'panda4.png'  # Replace with the correct path to the hover image 3

    window = SelectTestWindow(panda_image_path, eye_image_path, eye_image_path1, eye_image_path2, hover_image_path1, hover_image_path2, hover_image_path3)

    sys.exit(app.exec())
