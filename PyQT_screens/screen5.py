import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QSlider, QPushButton, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QLinearGradient, QColor, QPalette, QBrush, QPixmap

class SetValuesWindow3(QMainWindow):
    navigate_prev = pyqtSignal()  # Custom signal for navigation to the previous screen
    navigate_next = pyqtSignal(dict)  # Custom signal for navigation to the next screen
    slider_changed = pyqtSignal(str, int) 

    def __init__(self, panda_image_path, experiment_type, test_type):
        super().__init__()

        self.sliders = []
        self.labels = []
        self.experiment_type = experiment_type
        self.test_type = test_type

        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)
        main_widget.setLayout(main_layout)

        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setCoordinateMode(QLinearGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(189, 234, 204))
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(gradient))
        self.setPalette(palette)

        # Create title label
        self.title_label = QLabel("Set Values", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 60px; font-weight: bold; color: #008682; padding: 10px; background-color: #EBFFC5;")
        self.title_label.setFixedHeight(200)
        main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignTop)

        # Create a layout for sliders and panda image
        center_layout = QHBoxLayout()

        # Add stretch to center the content
        center_layout.addStretch(1)

        # Create a vertical layout for sliders
        self.slider_layout = QVBoxLayout()
        self.slider_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add stretch at the top to adjust vertical position
        self.slider_layout.addStretch(1)

        # Dynamically create sliders based on experiment type and test type
        self.create_experiment_sliders(experiment_type, test_type)

        # Add stretch at the bottom to adjust vertical position
        self.slider_layout.addStretch(1)

        center_layout.addLayout(self.slider_layout)

        # Add stretch to center the content
        center_layout.addStretch(1)

        # Load and set the panda image
        self.panda_label = QLabel(self)
        panda_pixmap = QPixmap(panda_image_path)
        self.panda_label.setPixmap(panda_pixmap.scaled(450, 450, Qt.AspectRatioMode.KeepAspectRatio))
        self.panda_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)
        center_layout.addWidget(self.panda_label, alignment=Qt.AlignmentFlag.AlignBottom)

        main_layout.addLayout(center_layout)

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
        self.next_button.clicked.connect(self.emit_all_slider_values)
        # self.next_button.clicked.connect(self.slider_changed.emit(slider.objectName(), value / 1000.0))

        main_layout.addLayout(nav_layout)

        # Set the central widget of the main window
        self.setCentralWidget(main_widget)

        # Remove window borders and show the window in full screen mode
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.showFullScreen()

    def create_slider(self, layout, label_text, min_val=0, max_val=1000, start_val=0, step=1):
        label = QLabel(label_text, self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #008682;")
        layout.addWidget(label)

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setMinimum(int(min_val * 1000))
        slider.setMaximum(int(max_val * 1000))
        slider.setValue(int(start_val * 1000))
        slider.setSingleStep(int(step * 1000))
        slider.setObjectName(label_text)
        slider.setFixedWidth(600)  # Set fixed width for the slider
        slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 16px;  /* Adjusted height for the groove */
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 #3498db, stop:1 #2980b9);  /* Gradient for the groove */
                border-radius: 8px;  /* Rounded corners for the groove */
            }
            QSlider::handle:horizontal {
                background: #ffffff;
                border: 1px solid #5c5c5c;
                width: 22px;  /* Width for the handle */
                height: 22px;  /* Height for the handle */
                margin: -3px 0;  /* Adjust margin for the larger handle */
                border-radius: 11px;  /* Rounded corners for the handle */
            }
            QSlider::add-page:horizontal {
                background: #cccccc;
                border: 1px solid #999999;
                height: 16px;  /* Adjusted height for the add-page */
                border-radius: 8px;  /* Rounded corners for the add-page */
            }
        """)
        slider.valueChanged.connect(self.slider_updation)
        layout.addWidget(label)
        layout.addWidget(slider)
        # self.sliders[label_text] = slider  # Store the slider with its label text as the key
        self.labels.append(label)
        self.sliders.append(slider)

    def slider_updation(self, value):
        slider = self.sender()
        self.slider_changed.emit(slider.objectName(), value / 1000.0)

    def create_experiment_sliders(self, experiment_type, test_type):
        if experiment_type == "Fixed Incrementor":
            if test_type == "Contrast Sensitivity":
                self.create_slider(self.slider_layout, "Min Contrast", 0, 1, 0.02, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Max Contrast", 0, 1, 1, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Spatial Frequency", 0, 10, 0.5, 0.001)

            elif test_type == "Spatial Frequency":
                self.create_slider(self.slider_layout, "Min Spatial Frequency", 0, 10, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Max Spatial Frequency", 0, 10, 5, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Contrast", 0, 1, 1, 0.001)

            elif test_type == "Vernier Acuity":
                self.create_slider(self.slider_layout, "Min Phase", 0, 1, 0.01, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Max Phase", 0, 1, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Contrast", 0, 1, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Spatial Frequency", 0, 1, 0.2, 0.001)

            elif test_type == "Spatial Phase":
                self.create_slider(self.slider_layout, "Min Phase", 0, 1, 0.01, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Max Phase", 0, 1, 0.5, 0.001)

        elif experiment_type == "Staircase":
            if test_type == "Contrast Sensitivity":
                self.create_slider(self.slider_layout, "Start Contrast", 0, 1, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Spatial Frequency", 0, 1, 1, 0.001)

            elif test_type == "Spatial Frequency":
                self.create_slider(self.slider_layout, "Start Spatial Frequency", 0, 10, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Contrast", 0, 10, 5, 0.001)

            elif test_type == "Vernier Acuity":
                self.create_slider(self.slider_layout, "Start Phase", 0, 1, 0.01, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Contrast", 0, 1, 0.2, 0.001)
                self.slider_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
                self.create_slider(self.slider_layout, "Spatial Frequency", 0, 1, 0.2, 0.001)
    
    def emit_all_slider_values(self):
        # Emit all slider values when the next button is clicked
        slider_values = {slider.objectName(): slider.value() / 1000.0 for slider in self.sliders}
        self.navigate_next.emit(slider_values)

    def get_slider_values(self):
        # Create a dictionary to store the slider values
        slider_values = {}
        # Iterate over the stored sliders and get their current values
        for label, slider in self.sliders.items():
            slider_values[label] = slider.value()
        return slider_values

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    panda_image_path = "panda6.png"  # Replace with your panda image path
    experiment_type = "Fixed Incrementor"  # Example value, replace with your logic
    test_type = "Contrast Sensitivity"  # Example value, replace with your logic
    eye_tracker_type = "Some Eye Tracker Type"  # Example value, replace with your logic

    window = SetValuesWindow3(panda_image_path, experiment_type, test_type)
    window.show()

    sys.exit(app.exec())