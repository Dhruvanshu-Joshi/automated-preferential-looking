import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from index import FullScreenWindow
from screen2 import SelectTestWindow # Assuming the code above is saved in select_test.py
from screen3 import SelectTestWindow2
from screen4 import SelectHemWindow
from screen5 import SetValuesWindow3
from screen6 import startWindow
from screen7 import ExpWindow
from screen8 import progressWindow

class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        # self.selected_values = {
        # "test": self.select_test_window.get_test(),
        # "experiment": self.select_screen3_window.get_exp(),
        # "eye_tracker": self.select_screen3_window.get_device(),
        # "hemisphere": self.select_screen3_window.get_hemisphere(),
        # # "min_var": self.min_scale.get(),
        # # "max_var": max_var,
        # # "param1": self.param1_scale.get(),
        # # "param2": param2,
        # }

        self.select_test_window = SelectTestWindow(
            "panda.png",
            "eye1.png",
            "eye2.png",
            "eye3.png",
            "panda2.png",
            "panda3.png",
            "panda4.png"
        )
        self.index_window = FullScreenWindow('image.png')
        self.select_screen3_window = SelectTestWindow2(
            "panda5.png",
            "eye1.png",
            "eye2.png",
            "eye3.png",
            "button1.png",
            "button2.png"
        )

        self.select_screen4_window = SelectHemWindow(
            "panda7.png",
            "eye1.png",
            "eye2.png",
            "eye3.png",
            "panda2.png",
            "panda3.png",
            "panda4.png"
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
        }

        # self.select_screen5_window = SetValuesWindow3(
        #     "panda6.png", self.selected_values["experiment"], self.selected_values["test"], self.selected_values["eye_tracker"]
        # )

        # self.exp_window = ExpWindow(
        #     "stimulus.png",
        #     "panda8.png"
        # )

        self.prog_window = progressWindow()

        self.addWidget(self.index_window)
        self.addWidget(self.select_test_window)
        self.addWidget(self.select_screen3_window)
        self.addWidget(self.select_screen4_window)
        # self.addWidget(self.select_screen5_window)
        # self.addWidget(self.start_window)
        # self.addWidget(self.exp_window)

        self.index_window.navigate_next.connect(self.show_test_window)
        self.select_test_window.navigate_prev.connect(self.show_index_window)
        # self.selected_values["test"] = self.select_test_window.get_test()
        self.select_test_window.navigate_next.connect(self.show_screen3_window)
        self.select_screen3_window.navigate_prev.connect(self.show_test_window)
        # self.selected_values["experiment"] = self.select_screen3_window.get_exp()
        # self.selected_values["eye_tracker"] = self.select_screen3_window.get_device()
        self.select_screen3_window.navigate_next.connect(self.show_screen4_window)
        self.select_screen5_window = SetValuesWindow3(
            "panda6.png", self.selected_values["experiment"], self.select_test_window.get_test(), self.selected_values["eye_tracker"]
        )
        self.select_screen4_window.navigate_prev.connect(self.show_screen3_window)
        # self.selected_values["hemisphere"] = self.select_screen4_window.get_hemisphere()
        # self.addWidget(self.select_screen5_window)
        self.select_screen4_window.navigate_next.connect(self.show_screen5_window)
        self.select_screen5_window.navigate_prev.connect(self.show_screen4_window)
        self.start_window = startWindow(
            "start.png", 
        )
        self.addWidget(self.start_window)
        self.select_screen5_window.navigate_next.connect(self.show_start_window)
        self.start_window.navigate_prev.connect(self.show_screen5_window)
        self.exp_window = ExpWindow(
            "stimulus.png",
            "panda8.png"
        )
        self.addWidget(self.exp_window)
        self.start_window.navigate_next.connect(self.show_exp_window)
        self.exp_window.navigate_next.connect(self.show_prog_window)

        self.prog_window = progressWindow()
        # self.addWidget(self.prog_window)

        self.setCurrentWidget(self.index_window)

        self.showFullScreen()

    def show_index_window(self):
        self.setCurrentWidget(self.index_window)
    
    def show_test_window(self):
        self.setCurrentWidget(self.select_test_window)
        # self.selected_values["test"] = self.select_test_window.get_test()
        # print(self.selected_values["test"]+" ")
        # assert 0
        
    def show_screen3_window(self):
        self.setCurrentWidget(self.select_screen3_window)
        # self.selected_values["experiment"] = self.select_screen3_window.get_exp()
        # self.selected_values["eye_tracker"] = self.select_screen3_window.get_device()

    def show_screen4_window(self):
        self.setCurrentWidget(self.select_screen4_window)
        # self.select_screen5_window = SetValuesWindow3(
        #     "panda6.png", self.selected_values["experiment"], self.select_test_window.get_test(), self.selected_values["eye_tracker"]
        # )
        # self.addWidget(self.select_screen5_window)
        # self.selected_values["hemisphere"] = self.select_screen4_window.get_hemisphere()

    def show_screen5_window(self):
        self.setCurrentWidget(self.select_screen5_window)

    def show_start_window(self):
        self.setCurrentWidget(self.start_window)

    def show_exp_window(self):
        self.setCurrentWidget(self.exp_window)

    def show_prog_window(self):
        self.setCurrentWidget(self.prog_window)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Q:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
