# import os
# os.environ['PSYCHOPY_USERAPPDATA'] = 'C:/Users/jmahe/AppData/Roaming/psychopy3'

# from predict import *
# import cv2
# # from icatcher.cli import *
# from psychopy import locale_setup
# from psychopy import prefs
# from psychopy import  gui, visual, core, data, event, logging, clock, colors, layout
# from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
#                                 STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

# import numpy as np  # whole numpy lib is available, prepend 'np.'
# from numpy import (sin, cos, tan, log, log10, pi, average,
#                    sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

# # import psychopy.iohub as io
# from psychopy.hardware import keyboard
# import matplotlib.pyplot as plt
# from psychometric_function import *
# import random
# import math
# import platform

# from psychopy import locale_setup
# from psychopy import prefs
# from psychopy import  gui, visual, core, data, event, logging, clock, colors, layout
# from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
#                                 STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

# import numpy as np  # whole numpy lib is available, prepend 'np.'
# from numpy import (sin, cos, tan, log, log10, pi, average,
#                    sqrt, std, deg2rad, rad2deg, linspace, asarray)
# from numpy.random import random, randint, normal, shuffle, choice as randchoice
# import os  # handy system and path functions
# import sys  # to get file system encoding

# # import psychopy.iohub as io
# from psychopy.hardware import keyboard
# import matplotlib.pyplot as plt
# from psychometric_function import *
# import random
# import math
# import platform

from PyQt6.QtWidgets import QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fixed_increment import *
from staircase import *
from psychometric_function import *
from fixed_increment_icatcher import *
from staircase_icatcher import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQT_screens.main import MainApp

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    app.exec()
    selected_values = main_app.start_experiment()
    del main_app

    if selected_values["experiment"]=="Fixed Incrementor":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                    print("case is 1")
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response= fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
            else:
                case='1'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
                
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
            else:
                case='3'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=fixedincrement_vernier(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
            else:
                case='5'
                feedback,value,response=fixedincrement_vernier_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
                
        psychometric_function(feedback,value,response)

    elif selected_values["experiment"]=="Staircase":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
            else:
                case='1'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"])
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
            else:
                case='3'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"])
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=staircase_vernier(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
            else:
                case='5'
                feedback,value,response=staircase_vernier_icatcher(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
        psychometric_function(feedback,value,case)

if __name__ == "__main__":
    main()