import sys
import os
from PyQt6.QtWidgets import QApplication, QStackedWidget
from PyQt6.QtCore import Qt, pyqtSignal
from .index import FullScreenWindow
from .screen2 import SelectTestWindow
from .screen3 import SelectTestWindow2
from .screen4 import SelectHemWindow
from .screen5 import SetValuesWindow3
from .screen6 import startWindow
from .screen7 import ExpWindow
from .screen8 import progressWindow
from .screen9 import SelectVideoSourceWindow  # Import Screen9

# Main application class inheriting from QStackedWidget
class MainApp(QStackedWidget):
    experiment_started = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Set up the script directory path
        self.script_dir = os.path.dirname(__file__)

        # Initialize SelectTestWindow with image paths
        self.select_test_window = SelectTestWindow(
            os.path.join(self.script_dir, "imgs/panda.png"),
            os.path.join(self.script_dir, "imgs/eye1.png"),
            os.path.join(self.script_dir, "imgs/eye2.png"),
            os.path.join(self.script_dir, "imgs/eye3.png"),
            os.path.join(self.script_dir, "imgs/panda2.png"),
            os.path.join(self.script_dir, "imgs/panda3.png"),
            os.path.join(self.script_dir, "imgs/panda4.png")
        )

        # Initialize FullScreenWindow with an image path
        self.index_window = FullScreenWindow(os.path.join(self.script_dir, 'imgs/image.png'))

        # Initialize SelectTestWindow2 with image paths
        self.select_screen3_window = SelectTestWindow2(
            os.path.join(self.script_dir, "imgs/panda5.png"),
            os.path.join(self.script_dir, "imgs/eye1.png"),
            os.path.join(self.script_dir, "imgs/eye2.png"),
            os.path.join(self.script_dir, "imgs/eye3.png"),
            os.path.join(self.script_dir, "imgs/button1.png"),
            os.path.join(self.script_dir, "imgs/button2.png")
        )
        
        # Determine the selected device and set eye_tracker accordingly       
        if self.select_screen3_window.get_device() == "Eye Tracker":
            eye_tracker = 0
        else:
            eye_tracker = 1

        # Initialize SelectHemWindow with image paths
        self.select_screen4_window = SelectHemWindow(
            os.path.join(self.script_dir, "imgs/panda7.png"),
            os.path.join(self.script_dir, "imgs/eye1.png"),
            os.path.join(self.script_dir, "imgs/eye2.png"),
            os.path.join(self.script_dir, "imgs/eye3.png"),
            os.path.join(self.script_dir, "imgs/panda2.png"),
            os.path.join(self.script_dir, "imgs/panda3.png"),
            os.path.join(self.script_dir, "imgs/panda4.png")
        )

        # Store selected values in a dictionary
        self.selected_values = {
            "test": self.select_test_window.get_test(),
            "experiment": self.select_screen3_window.get_exp(),
            "eye_tracker": self.select_screen3_window.get_device(),
            "hemisphere": self.select_screen4_window.get_hemisphere(),
            "min_var": 0,
            "max_var": 0,
            "param1": 0,
            "param2": 0,
            "video_file_path": 0,
        }

        # Add different screens (widgets) to the stacked widget
        self.addWidget(self.index_window)
        self.addWidget(self.select_test_window)
        self.addWidget(self.select_screen3_window)
        self.addWidget(self.select_screen4_window)

        # Connect signals to the respective slots (functions) to navigate between screens
        self.index_window.navigate_next.connect(self.show_test_window)
        self.select_test_window.navigate_prev.connect(self.show_index_window)
        self.select_test_window.navigate_next.connect(self.update_test_value)
        self.select_test_window.navigate_next.connect(self.show_screen3_window)
        self.select_screen3_window.navigate_prev.connect(self.show_test_window)
        self.select_screen3_window.navigate_next.connect(self.update_expdevice_value)
        self.select_screen3_window.navigate_next.connect(self.show_screen4_window)
        self.select_screen3_window.navigate_next.connect(self.update_screen5_obj)
        
        # Initialize SetValuesWindow3 with image and selected experiment/test
        self.select_screen5_window = SetValuesWindow3(
            os.path.join(self.script_dir, "imgs/panda6.png"), 
            self.selected_values["experiment"], 
            self.selected_values['test']
        )
        self.addWidget(self.select_screen5_window)

        # Connect navigation for screens 4 and 5
        self.select_screen4_window.navigate_prev.connect(self.show_screen3_window)
        self.select_screen4_window.navigate_next.connect(self.update_hemisphere_value)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
        self.select_screen5_window.navigate_prev.connect(self.show_screen4_window_onprev)

        # Initialize the start window        
        self.start_window = startWindow(os.path.join(self.script_dir, "imgs/start.png"))
        self.addWidget(self.start_window)

        # Add Screen9 before startWindow
        self.screen9_window = SelectVideoSourceWindow()
        self.addWidget(self.screen9_window)

        # Connect navigation and data handling for screen 9 and the start window        
        self.select_screen5_window.navigate_next.connect(self.handle_slider_dictionary)
        self.select_screen5_window.navigate_next.connect(self.show_screen9_window)
        self.screen9_window.navigate_prev.connect(self.show_screen5_window)
        self.screen9_window.navigate_next.connect(self.show_start_window)
        self.screen9_window.navigate_next.connect(self.get_camera_or_video)
        self.start_window.navigate_prev.connect(self.show_screen9_window)

        # Connect the final start button to the experiment start        
        self.start_window.navigate_next.connect(self.start_experiment)

        # Set the current widget to the index window (initial screen)
        self.setCurrentWidget(self.index_window)

        # Show the application in fullscreen mode
        self.showFullScreen()

    # Update the selected test value based on user input
    def update_test_value(self, test):
        self.selected_values["test"] = test
        print(f"Test selected: {self.selected_values['test']}")

    # Update selected experiment and device values based on user input
    def update_expdevice_value(self, exp, device):
        self.selected_values["experiment"] = exp
        self.selected_values["eye_tracker"] = device
        print(f"Experiment selected: {self.selected_values['experiment']} and Device selected: {self.selected_values['eye_tracker']}")

    # Update the selected hemisphere value based on user input
    def update_hemisphere_value(self, hem):
        self.selected_values["hemisphere"] = hem
        print(f"Hemisphere selected: {self.selected_values['hemisphere']}")

    # Reinitialize and add the screen 5 widget with updated values
    def update_screen5_obj(self):
        self.select_screen5_window = SetValuesWindow3(
            os.path.join(self.script_dir, "imgs/panda6.png"), 
            self.selected_values["experiment"], 
            self.selected_values['test']
        )
        self.addWidget(self.select_screen5_window)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
        self.select_screen5_window.navigate_prev.connect(self.show_screen4_window_onprev)
        self.select_screen5_window.navigate_next.connect(self.handle_slider_dictionary)
        self.select_screen5_window.navigate_next.connect(self.show_screen9_window)
        self.screen9_window.navigate_next.connect(self.show_start_window)

    # Set the selected video file path or camera based on user input
    def get_camera_or_video(self, path):
        if path=="camera":
            self.selected_values["video_file_path"] = 0
        else:
            self.selected_values["video_file_path"] = path
        print(f"Video selected: {self.selected_values['video_file_path']}")

    # Handle slider dictionary to update min/max variables and parameters
    def handle_slider_dictionary(self, slider_dict):
        print("Received slider dictionary:", slider_dict)
        for slider_name in slider_dict:
            if(self.selected_values['experiment'] == "Fixed Incrementor"):
                if(self.selected_values['test'] == "Contrast Sensitivity"):
                    self.selected_values['min_var'] = slider_dict['Min Contrast']
                    self.selected_values['max_var'] = slider_dict['Max Contrast']
                    self.selected_values['param1'] = slider_dict['Spatial Frequency']
                    self.selected_values['param2'] = 0
                elif(self.selected_values['test'] == "Spatial Frequency"):
                    self.selected_values['min_var'] = slider_dict['Min Spatial Frequency']
                    self.selected_values['max_var'] = slider_dict['Max Spatial Frequency']
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = 0
                elif(self.selected_values['test'] == "Vernier Acuity"):
                    self.selected_values['min_var'] = slider_dict['Min Phase']
                    self.selected_values['max_var'] = slider_dict['Max Phase']
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = slider_dict['Spatial Frequency']
            elif(self.selected_values['experiment'] == "Staircase"):
                if(self.selected_values['test'] == "Contrast Sensitivity"):
                    self.selected_values['min_var'] = slider_dict['Start Contrast']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Spatial Frequency']
                    self.selected_values['param2'] = 0
                elif(self.selected_values['test'] == "Spatial Frequency"):
                    self.selected_values['min_var'] = slider_dict['Start Spatial Frequency']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = 0
                elif(self.selected_values['test'] == "Vernier Acuity"):
                    self.selected_values['min_var'] = slider_dict['Start Phase']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = slider_dict['Spatial Frequency']

    # Navigation methods to switch between screens    
    def show_index_window(self):
        self.setCurrentWidget(self.index_window)
    
    def show_test_window(self):
        self.setCurrentWidget(self.select_test_window)
        
    def show_screen3_window(self):
        self.setCurrentWidget(self.select_screen3_window)

    def show_screen4_window(self, exp, device):
        # self.select_screen4_window.clear_buttons()
        self.select_screen4_window = SelectHemWindow(
            os.path.join(self.script_dir, "imgs/panda7.png"),
            os.path.join(self.script_dir, "imgs/eye1.png"),
            os.path.join(self.script_dir, "imgs/eye2.png"),
            os.path.join(self.script_dir, "imgs/eye3.png"),
            os.path.join(self.script_dir, "imgs/panda2.png"),
            os.path.join(self.script_dir, "imgs/panda3.png"),
            os.path.join(self.script_dir, "imgs/panda4.png")
        )
        self.addWidget(self.select_screen4_window)
        self.select_screen4_window.set_mode(exp, device, os.path.join(self.script_dir, "imgs/eye1.png"), os.path.join(self.script_dir, "imgs/eye2.png"))
        self.select_screen4_window.navigate_prev.connect(self.show_screen3_window)
        self.select_screen4_window.navigate_next.connect(self.update_hemisphere_value)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)

        self.setCurrentWidget(self.select_screen4_window)
    
    def show_screen4_window_onprev(self):
        self.setCurrentWidget(self.select_screen4_window)

    def show_screen5_window(self):
        self.setCurrentWidget(self.select_screen5_window)

    def show_screen9_window(self):
        self.setCurrentWidget(self.screen9_window)

    def show_start_window(self):
        self.setCurrentWidget(self.start_window)

    def start_experiment(self):
        # Code to start the experiment
        pass
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

    def start_experiment(self):
        self.close()
        return self.selected_values

    def close_gui(self):
        self.start_experiment()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
