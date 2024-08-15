import sys
import os
from PyQt6.QtWidgets import QApplication, QStackedWidget
from PyQt6.QtCore import Qt, pyqtSignal
from .index import FullScreenWindow
from .screen2 import SelectTestWindow # Assuming the code above is saved in select_test.py
from .screen3 import SelectTestWindow2
from .screen4 import SelectHemWindow
from .screen5 import SetValuesWindow3
from .screen6 import startWindow
from .screen7 import ExpWindow
from .screen8 import progressWindow

class MainApp(QStackedWidget):
    experiment_started = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.script_dir = os.path.dirname(__file__)  # Get the directory of the current script
        self.select_test_window = SelectTestWindow(
            os.path.join(self.script_dir, "panda.png"),
            os.path.join(self.script_dir, "eye1.png"),
            os.path.join(self.script_dir, "eye2.png"),
            os.path.join(self.script_dir, "eye3.png"),
            os.path.join(self.script_dir, "panda2.png"),
            os.path.join(self.script_dir, "panda3.png"),
            os.path.join(self.script_dir, "panda4.png")
        )
        # image_path = os.path.join(self.script_dir, 'image.png')
        self.index_window = FullScreenWindow(os.path.join(self.script_dir, 'image.png'))
        self.select_screen3_window = SelectTestWindow2(
            os.path.join(self.script_dir, "panda5.png"),
            os.path.join(self.script_dir, "eye1.png"),
            os.path.join(self.script_dir, "eye2.png"),
            os.path.join(self.script_dir, "eye3.png"),
            os.path.join(self.script_dir, "button1.png"),
            os.path.join(self.script_dir, "button2.png")
        )

        self.select_screen4_window = SelectHemWindow(
            os.path.join(self.script_dir, "panda7.png"),
            os.path.join(self.script_dir, "eye1.png"),
            os.path.join(self.script_dir, "eye2.png"),
            os.path.join(self.script_dir, "eye3.png"),
            os.path.join(self.script_dir, "panda2.png"),
            os.path.join(self.script_dir, "panda3.png"),
            os.path.join(self.script_dir, "panda4.png")
        )

        self.selected_values = {
        "test": self.select_test_window.get_test(),
        "experiment": self.select_screen3_window.get_exp(),
        "eye_tracker": self.select_screen3_window.get_device(),
        "hemisphere": self.select_screen4_window.get_hemisphere(),
        # "min_var": self.min_scale.get(),
        # "max_var": max_var,
        # "param1": self.param1_scale.get(),
        # "param2": param2,
        "min_var": 0,
        "max_var": 0,
        "param1": 0,
        "param2": 0,
        }

        # self.prog_window = progressWindow()

        self.addWidget(self.index_window)
        self.addWidget(self.select_test_window)
        self.addWidget(self.select_screen3_window)
        self.addWidget(self.select_screen4_window)

        self.index_window.navigate_next.connect(self.show_test_window)
        self.select_test_window.navigate_prev.connect(self.show_index_window)
        self.select_test_window.navigate_next.connect(self.update_test_value)  # Connect to new slot
        self.select_test_window.navigate_next.connect(self.show_screen3_window)
        self.select_screen3_window.navigate_prev.connect(self.show_test_window)
        self.select_screen3_window.navigate_next.connect(self.update_expdevice_value)
        self.select_screen3_window.navigate_next.connect(self.show_screen4_window)
        # print()
        # print(self.selected_values["experiment"]+" "+self.selected_values['test']+" "+self.selected_values["eye_tracker"])
        # print()
        self.select_screen3_window.navigate_next.connect(self.update_screen5_obj)
        self.select_screen5_window = SetValuesWindow3(
            os.path.join(self.script_dir, "panda6.png"), self.selected_values["experiment"], self.selected_values['test']
        )
        self.addWidget(self.select_screen5_window)
        self.select_screen4_window.navigate_prev.connect(self.show_screen3_window)
        self.select_screen4_window.navigate_next.connect(self.update_hemisphere_value)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
        # self.select_screen5_window.slider_changed.connect(self.update_slider_value)
        self.select_screen5_window.navigate_prev.connect(self.show_screen4_window)
        self.start_window = startWindow(
            os.path.join(self.script_dir, "start.png"), 
        )
        self.addWidget(self.start_window)
        self.select_screen5_window.navigate_next.connect(self.handle_slider_dictionary)
        self.select_screen5_window.navigate_next.connect(self.show_start_window)
        self.start_window.navigate_prev.connect(self.show_screen5_window)
        # self.exp_window = ExpWindow(
        #     os.path.join(self.script_dir, "stimulus.png"),
        #     os.path.join(self.script_dir, "panda8.png")
        # )
        # self.addWidget(self.exp_window)
        # self.start_window.navigate_next.connect(self.close_gui)
        # self.exp_window.navigate_next.connect(self.show_prog_window)

        # self.prog_window = progressWindow()
        self.start_window.navigate_next.connect(self.start_experiment)  # Connect button click to function
        self.setCurrentWidget(self.index_window)

        self.showFullScreen()

    def update_test_value(self, test):
        self.selected_values["test"] = test
        print(f"Test selected: {self.selected_values['test']}")  # For debugging purposes

    def update_expdevice_value(self, exp, device):
        self.selected_values["experiment"] = exp
        self.selected_values["eye_tracker"] = device
        print(f"Experiment selected: {self.selected_values['experiment']} and Device selected: {self.selected_values['eye_tracker']}")

    def update_hemisphere_value(self, hem):
        self.selected_values["hemisphere"] = hem
        print(f"Hemisphere selected: {self.selected_values['hemisphere']}")

    def update_screen5_obj(self):
        self.select_screen5_window = SetValuesWindow3(
            os.path.join(self.script_dir, "panda6.png"), self.selected_values["experiment"], self.selected_values['test']
        )
        self.addWidget(self.select_screen5_window)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
        # self.select_screen5_window.slider_changed.connect(self.update_slider_value)
        self.select_screen5_window.navigate_prev.connect(self.show_screen4_window)
        self.select_screen5_window.navigate_next.connect(self.handle_slider_dictionary)
        self.select_screen5_window.navigate_next.connect(self.show_start_window)
        self.start_window.navigate_prev.connect(self.show_screen5_window)

    # def update_slider_value(self, slider_name, value):
    #     if "Min" in slider_name:
    #         self.selected_values["min_var"] = value
    #     elif "Max" in slider_name:
    #         self.selected_values["max_var"] = value
    #     elif "Start" in slider_name:
    #         self.selected_values["min_var"] = value
    #         self.selected_values["max_var"] = 0
    #     elif "Spatial frequency" in slider_name:
    #         self.selected_values["param1"] = value
    #     elif "Contrast" in slider_name:
    #         self.selected_values["param1"] = value if self.selected_values["param1"] is None else self.selected_values["param2"]
    #     elif "Spatial Frequency" in slider_name:
    #         self.selected_values["param2"] = value
    #     elif "Phase" in slider_name:
    #         self.selected_values["min_var"] = value if self.selected_values["min_var"] is None else self.selected_values["param1"]

    #     print(f"Slider {slider_name} moved: {value}, updated values: {self.selected_values}")

    def handle_slider_dictionary(self, slider_dict):
        # Handle the slider dictionary emitted by SetValuesWindow3
        print("Received slider dictionary:", slider_dict)
        # for slider_name in slider_dict:
        #     if "Min" in slider_name:
        #         self.selected_values["min_var"] = slider_dict[slider_name]
        #     elif "Max" in slider_name:
        #         self.selected_values["max_var"] = slider_dict[slider_name]
        #     elif "Start" in slider_name:
        #         self.selected_values["min_var"] = slider_dict[slider_name]
        #         self.selected_values["max_var"] = 0
        #     elif "Spatial frequency" in slider_name:
        #         self.selected_values["param1"] = slider_dict[slider_name]
        #     elif "Contrast" in slider_name:
        #         self.selected_values["param1"] = slider_dict[slider_name] if self.selected_values["param1"] is None else self.selected_values["param2"]
        #     elif "Spatial Frequency" in slider_name:
        #         self.selected_values["param2"] = slider_dict[slider_name]
        #     elif "Phase" in slider_name:
        #         self.selected_values["min_var"] = slider_dict[slider_name] if self.selected_values["min_var"] is None else self.selected_values["param1"]
        for slider_name in slider_dict:
            if(self.selected_values['experiment']=="Fixed Incrementor"):
                if(self.selected_values['test']=="Contrast Sensitivity"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Min Contrast:")
                    # self.min_scale.set(0.02)
                    # self.min_scale.pack()
                    self.selected_values['min_var'] = slider_dict['Min Contrast']
                    self.selected_values['max_var'] = slider_dict['Max Contrast']
                    self.selected_values['param1'] = slider_dict['Spatial Frequency']
                    self.selected_values['param2'] = 0

                    # # Create a Scale widget for controlling the maximum value
                    # self.max_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Max Contrast:")
                    # self.max_scale.set(1)
                    # self.max_scale.pack()

                    # # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial frequency:")
                    # self.param1_scale.set(0.5)
                    # self.param1_scale.pack()

        
                elif(self.selected_values['test']=="Spatial Frequency"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Min Spatial Frequency:")
                    # self.min_scale.set(0.2)  
                    # self.min_scale.pack()

                    # # Create a Scale widget for controlling the maximum value
                    # self.max_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Max Spatial Frequency:")
                    # self.max_scale.set(5)
                    # self.max_scale.pack()

                    # # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                    # self.param1_scale.set(1)
                    # self.param1_scale.pack()
                    self.selected_values['min_var'] = slider_dict['Min Spatial Frequency']
                    self.selected_values['max_var'] = slider_dict['Max Spatial Frequency']
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = 0

                elif(self.selected_values['test']=="Vernier Acuity"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Min Phase:")
                    # self.min_scale.set(0.01)  
                    # self.min_scale.pack()

                    # # Create a Scale widget for controlling the maximum value
                    # self.max_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Max Phase:")
                    # self.max_scale.set(1)
                    # self.max_scale.pack()

                    # # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                    # self.param1_scale.set(1)
                    # self.param1_scale.pack()

                    # # Create a Scale widget for controlling param2 value
                    # self.param2_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial Frequency")
                    # self.param2_scale.set(1)
                    # self.param2_scale.pack()
                    self.selected_values['min_var'] = slider_dict['Min Phase']
                    self.selected_values['max_var'] = slider_dict['Max Phase']
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = slider_dict['Spatial Frequency']
                    # self.min_var = self.min_scale.get()
                    # self.max_var = self.max_scale.get()
                    # self.param1 = self.param1_scale.get()
                    # self.param2 = self.param2_scale.get()
            elif(self.selected_values['experiment']=="Staircase"):
                if(self.selected_values['test']=="Contrast Sensitivity"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Start Contrast:")
                    # self.min_scale.set(0.5)
                    # self.min_scale.pack()

                    self.selected_values['min_var'] = slider_dict['Start Contrast']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Spatial Frequency']
                    self.selected_values['param2'] = 0

                    # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial frequency:")
                    # self.param1_scale.set(0.5)
                    # self.param1_scale.pack()

        
                elif(self.selected_values['test']=="Spatial Frequency"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Start Spatial Frequency:")
                    # self.min_scale.set(5)  
                    # self.min_scale.pack()

            
                    # # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                    # self.param1_scale.set(1)
                    # self.param1_scale.pack()

                    # self.max_scale.set(0)
                    # self.param2_scale(0)
                    self.selected_values['min_var'] = slider_dict['Start Spatial Frequency']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = 0
                elif(self.selected_values['test']=="Vernier Acuity"):
                    # self.min_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Start Phase:")
                    # self.min_scale.set(0.5)  
                    # self.min_scale.pack()

                    # # Create a Scale widget for controlling param1 value
                    # self.param1_scale = tk.Scale(self.screen4, from_=0, to=1, resolution=0.001, orient=tk.HORIZONTAL, label="Contrast:")
                    # self.param1_scale.set(1)
                    # self.param1_scale.pack()

                    # # Create a Scale widget for controlling param2 value
                    # self.param2_scale = tk.Scale(self.screen4, from_=0, to=10, resolution=0.001, orient=tk.HORIZONTAL, label="Spatial Frequency")
                    # self.param2_scale.set(1)
                    # self.param2_scale.pack()
                    self.selected_values['min_var'] = slider_dict['Start Phase']
                    self.selected_values['max_var'] = 0
                    self.selected_values['param1'] = slider_dict['Contrast']
                    self.selected_values['param2'] = slider_dict['Spatial Frequency']
        # assert 0
    
    def show_index_window(self):
        self.setCurrentWidget(self.index_window)
    
    def show_test_window(self):
        self.setCurrentWidget(self.select_test_window)
        
    def show_screen3_window(self):
        self.setCurrentWidget(self.select_screen3_window)

    def show_screen4_window(self):
        self.setCurrentWidget(self.select_screen4_window)

    def show_screen5_window(self):
        self.setCurrentWidget(self.select_screen5_window)

    def show_start_window(self):
        self.setCurrentWidget(self.start_window)

    def show_exp_window(self):
        self.setCurrentWidget(self.exp_window)


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

# import sys
# from PyQt6.QtWidgets import QApplication, QStackedWidget
# from PyQt6.QtCore import Qt
# from index import FullScreenWindow
# from screen2 import SelectTestWindow  # Assuming the code above is saved in select_test.py
# from screen3 import SelectTestWindow2
# from screen4 import SelectHemWindow
# from screen5 import SetValuesWindow3
# from screen6 import startWindow
# from screen7 import ExpWindow
# from screen8 import progressWindow

# class MainApp(QStackedWidget):
#     def __init__(self):
#         super().__init__()

#         self.selected_values = {
#             "test": None,
#             "experiment": None,
#             "eye_tracker": None,
#             "hemisphere": None,
#             "min_var": None,
#             "max_var": None,
#             "param1": None,
#             "param2": None,
#         }

#         self.index_window = FullScreenWindow('image.png')
#         self.select_test_window = SelectTestWindow(
#             "panda.png",
#             "eye1.png",
#             "eye2.png",
#             "eye3.png",
#             "panda2.png",
#             "panda3.png",
#             "panda4.png"
#         )
#         self.select_screen3_window = SelectTestWindow2(
#             "panda5.png",
#             "eye1.png",
#             "eye2.png",
#             "eye3.png",
#             "button1.png",
#             "button2.png"
#         )
#         self.select_screen4_window = SelectHemWindow(
#             "panda7.png",
#             "eye1.png",
#             "eye2.png",
#             "eye3.png",
#             "panda2.png",
#             "panda3.png",
#             "panda4.png"
#         )
#         # self.select_screen5_window = None  # Initialize as None until needed
#         self.select_screen5_window = SetValuesWindow3(
#             "panda6.png", self.selected_values["experiment"], self.selected_values['test']
#         )
#         self.start_window = startWindow("start.png")
#         self.exp_window = ExpWindow("stimulus.png", "panda8.png")
#         self.prog_window = progressWindow()

#         # Add all windows to the QStackedWidget
#         self.addWidget(self.index_window)
#         self.addWidget(self.select_test_window)
#         self.addWidget(self.select_screen3_window)
#         self.addWidget(self.select_screen4_window)
#         self.addWidget(self.select_screen5_window)
#         self.addWidget(self.start_window)
#         self.addWidget(self.exp_window)
#         # self.addWidget(self.prog_window)

#         # Connect signals to slots
#         self.index_window.navigate_next.connect(self.show_test_window)
#         self.select_test_window.navigate_prev.connect(self.show_index_window)
#         self.select_test_window.navigate_next.connect(self.update_test_value)
#         self.select_test_window.navigate_next.connect(self.show_screen3_window)
#         self.select_screen3_window.navigate_prev.connect(self.show_test_window)
#         self.select_screen3_window.navigate_next.connect(self.update_expdevice_value)
        
#         self.select_screen3_window.navigate_next.connect(self.update_screen5_obj)
#         self.select_screen3_window.navigate_next.connect(self.show_screen4_window)
        
#         self.select_screen4_window.navigate_prev.connect(self.show_screen3_window)
#         self.select_screen4_window.navigate_next.connect(self.update_hemisphere_value)
#         self.select_screen4_window.navigate_next.connect(self.show_screen5_window)

#         self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
#         self.select_screen5_window.navigate_prev.connect(self.update_screen5_obj)
#         self.select_screen5_window.navigate_prev.connect(self.show_screen4_window)

#         self.start_window.navigate_prev.connect(self.show_screen5_window)
#         self.start_window.navigate_next.connect(self.show_exp_window)
#         self.exp_window.navigate_next.connect(self.show_prog_window)

#         # Set the initial window
#         self.setCurrentWidget(self.index_window)
#         self.showFullScreen()

#     def update_test_value(self):
#         self.selected_values["test"] = self.select_test_window.get_test()
#         print(f"Test selected: {self.selected_values['test']}")  # For debugging purposes

#     def update_expdevice_value(self):
#         self.selected_values["experiment"] = self.select_screen3_window.get_exp()
#         self.selected_values["eye_tracker"] = self.select_screen3_window.get_device()
#         print(f"Experiment selected: {self.selected_values['experiment']} and Device selected: {self.selected_values['eye_tracker']}")

#     def update_hemisphere_value(self):
#         self.selected_values["hemisphere"] = self.select_screen4_window.get_hemisphere()
#         print(f"Hemisphere selected: {self.selected_values['hemisphere']}")

#     def update_screen5_obj(self):
#         experiment_type = self.selected_values["experiment"]
#         test_type = self.selected_values["test"]
#         eye_tracker = self.selected_values["eye_tracker"]
#         self.select_screen5_window = SetValuesWindow3("panda6.png", experiment_type, test_type)
#         self.addWidget(self.select_screen5_window)
#         self.select_screen5_window.navigate_prev.connect(self.show_screen4_window)
#         self.select_screen5_window.navigate_next.connect(self.collect_slider_values)
#         self.start_window.navigate_prev.connect(self.show_screen5_window)

#     def collect_slider_values(self):
#         if self.select_screen5_window:
#             slider_values = self.select_screen5_window.get_slider_values()
#             self.selected_values.update(slider_values)
#         self.show_start_window()

#     def show_index_window(self):
#         self.setCurrentWidget(self.index_window)

#     def show_test_window(self):
#         self.setCurrentWidget(self.select_test_window)

#     def show_screen3_window(self):
#         self.setCurrentWidget(self.select_screen3_window)

#     def show_screen4_window(self):
#         self.setCurrentWidget(self.select_screen4_window)

#     def show_screen5_window(self):
#         self.setCurrentWidget(self.select_screen5_window)

#     def show_start_window(self):
#         self.setCurrentWidget(self.start_window)

#     def show_exp_window(self):
#         self.setCurrentWidget(self.exp_window)

#     def show_prog_window(self):
#         self.setCurrentWidget(self.prog_window)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key.Key_Q:
#             self.close()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_app = MainApp()
#     main_app.show()
#     sys.exit(app.exec())
