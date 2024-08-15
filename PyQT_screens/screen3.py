import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon, QLinearGradient, QPalette, QColor, QBrush, QGradient, QPainter, QPen
from PyQt6.QtCore import Qt, QSize, pyqtSignal, QRect
import math

class SelectTestWindow2(QMainWindow):
    navigate_prev = pyqtSignal()  # Custom signal for navigation to the previous screen
    navigate_next = pyqtSignal(str, str)  # Custom signal for navigation to the next screen

    def __init__(self, panda_image_path, eye_image_path1, eye_image_path2, eye_image_path3, device_image_path, tracker_image_path):
        super().__init__()
        self.selected_experiment = None  # Initialize selected test to None
        self.selected_device = None
        self.selected_experiment_button = None
        self.selected_device_button = None

        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(208, 244, 229))
        gradient.setColorAt(1.0, QColor(189, 234, 204))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Create title label
        self.title_label = QLabel("Select Experiment", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #008682; padding: 10px; background-color: #EBFFC5;")
        self.title_label.setFixedHeight(100)
        main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Add stretch to push content to the center
        main_layout.addStretch(1)

        # Create the horizontal layout for the buttons and panda image
        center_layout = QHBoxLayout()

        # Add stretch to center the content
        center_layout.addStretch(1)

        # Create a vertical layout for the test buttons
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Create test buttons with eye images as visual pointers
        eye_pixmap1 = QPixmap(eye_image_path1).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
        self.create_test_button(button_layout, eye_pixmap1, "Staircase", "#05703c", "#fefefe", 0)
        button_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        eye_pixmap2 = QPixmap(eye_image_path2).scaled(60, 60, Qt.AspectRatioMode.KeepAspectRatio)
        self.create_test_button(button_layout, eye_pixmap2, "Fixed Incrementor", "#0258B2", "#DBFAF6", 1)

        center_layout.addLayout(button_layout)
        center_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Load and set the panda image
        self.panda_label = QLabel(self)
        panda_pixmap = QPixmap(panda_image_path)
        self.panda_label.setPixmap(panda_pixmap.scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio))
        self.panda_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        center_layout.addWidget(self.panda_label)

        main_layout.addLayout(center_layout)

        # Add stretch to push content to the center
        main_layout.addStretch(1)

        # Add the "Select Eye Tracker Type" button
        self.select_tracker_button = QPushButton("Select Eye Tracker Type", self)
        self.select_tracker_button.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                font-weight: bold;
                color: white;
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 black, stop:1 #05703c
                );
                padding: 10px 20px;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #023700, stop:1 #046A36
                );
            }
            QPushButton:pressed {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #023700, stop:1 #034C28
                );
            }
        """)
        self.select_tracker_button.setFixedSize(300, 60)
        self.select_tracker_button.setCursor(Qt.CursorShape.PointingHandCursor)
        main_layout.addWidget(self.select_tracker_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the horizontal layout for the device type buttons
        device_layout = QHBoxLayout()

        # Add stretch to center the content
        device_layout.addStretch(1)

        # Create device type buttons with images
        self.device_button = self.create_device_button(device_layout, device_image_path, "Eye tracker")
        # device_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        screen_size = QApplication.primaryScreen().size()
        device_layout.addSpacerItem(QSpacerItem(screen_size.width()//2, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        self.tracker_button = self.create_device_button(device_layout, tracker_image_path, "Eye Tracking Model")

        # Add stretch to center the content
        device_layout.addStretch(1)

        main_layout.addLayout(device_layout)

        # Add navigation buttons layout
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
        # self.next_button.clicked.connect(self.navigate_next.emit(self.selected_experiment, self.selected_device))

        self.next_button.clicked.connect(self.on_next_button_clicked)
        main_layout.addLayout(nav_layout)

        # Set the central widget of the main window
        self.setCentralWidget(main_widget)

        self.prev_button.clicked.connect(self.navigate_prev.emit)

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
                border-radius: 10px;
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

        button.clicked.connect(lambda: self.on_exp_button_click(button, text))  # Connect button click to method

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

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine)
        painter.setPen(pen)

        # Draw line from the center of select_button to the center of device_button and tracker_button
        select_button_rect = self.select_tracker_button.geometry()
        device_button_rect = self.device_button.geometry()
        tracker_button_rect = self.tracker_button.geometry()

        select_center_x = select_button_rect.center().x()
        select_center_y = select_button_rect.bottom()

        device_center_x = device_button_rect.center().x()
        device_center_y = device_button_rect.top()

        tracker_center_x = tracker_button_rect.center().x()
        tracker_center_y = tracker_button_rect.top()

        # Line to device button
        painter.drawLine(select_center_x, select_center_y, device_center_x, device_center_y)

        # Line to tracker button
        painter.drawLine(select_center_x, select_center_y, tracker_center_x, tracker_center_y)

        # Draw arrows
        self.draw_arrow(painter, select_center_x, select_center_y, device_center_x, device_center_y)
        self.draw_arrow(painter, select_center_x, select_center_y, tracker_center_x, tracker_center_y)

    def draw_arrow(self, painter, x1, y1, x2, y2):
        angle = 3.14 / 6  # 30 degrees
        length = 20  # arrow length

        line_dx = x2 - x1
        line_dy = y2 - y1
        line_length = (line_dx ** 2 + line_dy ** 2) ** 0.5

        norm_dx = line_dx / line_length
        norm_dy = line_dy / line_length

        left_arrow_x = x2 - length * (norm_dx * math.cos(angle) - norm_dy * math.sin(angle))
        left_arrow_y = y2 - length * (norm_dy * math.cos(angle) + norm_dx * math.sin(angle))
        right_arrow_x = x2 - length * (norm_dx * math.cos(angle) + norm_dy * math.sin(angle))
        right_arrow_y = y2 - length * (norm_dy * math.cos(angle) - norm_dx * math.sin(angle))

        painter.drawLine(int(x2), int(y2), int(left_arrow_x), int(left_arrow_y))
        painter.drawLine(int(x2), int(y2), int(right_arrow_x), int(right_arrow_y))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

    def create_device_button(self, layout, image_path, text):
        button_layout = QVBoxLayout()

        button = QPushButton(self)
        button.setIcon(QIcon(image_path))
        button.setIconSize(QSize(300, 150))
        button.setFixedSize(300, 150)
        button.setCursor(Qt.CursorShape.PointingHandCursor)

        label = QLabel(text, self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # if text == "Eye tracking Device":
        #     label.setAlignment(Qt.AlignmentFlag.AlignRight)
        # else:
        #     label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #008682;")

        button.clicked.connect(lambda: self.on_device_button_click(button, text))  # Connect button click to method

        button_layout.addWidget(button)
        button_layout.addWidget(label)

        layout.addLayout(button_layout)

        return button

    def on_exp_button_click(self, button, text):
        if self.selected_experiment_button:
            self.selected_experiment_button.setEnabled(True)  # Enable the previously selected button
            self.selected_experiment_button.setStyleSheet(self.selected_experiment_button.styleSheet().replace("darkgray", "white"))

        button.setEnabled(False)  # Disable the clicked button
        button.setStyleSheet(button.styleSheet().replace("white", "darkgray"))  # Darken the disabled button
        self.selected_experiment_button = button  # Update the selected button
        self.selected_experiment = text  # Update the selected test
        print(f"{text} button clicked!")

    def on_device_button_click(self, button, text):
        if self.selected_device_button:
            self.selected_device_button.setEnabled(True)  # Enable the previously selected button
            self.selected_device_button.setStyleSheet(self.selected_device_button.styleSheet().replace("darkgray", "white"))

        button.setEnabled(False)  # Disable the clicked button
        button.setStyleSheet(button.styleSheet().replace("white", "darkgray"))  # Darken the disabled button
        self.selected_device_button = button  # Update the selected button
        self.selected_device = text  # Update the selected test
        print(f"{text} button clicked!")

    def on_next_button_clicked(self):
        if self.selected_experiment and self.selected_device:
            self.navigate_next.emit(self.selected_experiment, self.selected_device)
        else:
            print("No device or exp selected!")

    def get_exp(self):
        # if not self.selected_experiment_button:
        #     raise ValueError('Please choose button corresponding to the test-experiment that you wish to perform')
        return self.selected_experiment_button

    def get_device(self):
        # if not self.selected_device_button:
        #     raise ValueError('Please choose button corresponding to the device that you wish to use to perform eye tracking')
        return self.selected_device_button

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Paths to the provided images
    panda_image_path = 'panda5.png'
    eye_image_path1 = 'eye1.png'  # Replace with the correct path to the eye image 1
    eye_image_path2 = 'eye2.png'  # Replace with the correct path to the eye image 2
    eye_image_path3 = 'eye3.png'  # Replace with the correct path to the eye image 3
    device_image_path = 'button1.png'  # Replace with the correct path to the device image
    tracker_image_path = 'button2.png'  # Replace with the correct path to the tracker image

    window = SelectTestWindow2(panda_image_path, eye_image_path1, eye_image_path2, eye_image_path3, device_image_path, tracker_image_path)

    sys.exit(app.exec())
