import os  # handy system and path functions
import sys  # to get file system encoding

from PyQt6.QtWidgets import QApplication

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from fixed_increment import *
from staircase import *
from psychometric_function import *
from fixed_increment_icatcher import fixedincrement_icatcher, fixedincrement_vernier_icatcher
from staircase_icatcher import staircase_icatcher, staircase_vernier_icatcher
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyQT_screens.main import MainApp

def main():
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    app.exec()
    selected_values = main_app.start_experiment()
    del main_app

    #TODO: Add pyqt screen for saved_video and camera option
    if selected_values["video_file_path"]!=0:
        path=selected_values["video_file_path"]
    else:
        path=0
    if selected_values["experiment"]=="Fixed Incrementor":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                    print("case is 1")
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response= fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
                psychometric_function(feedback,value,response, None)
            else:
                case='1'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"], path)
                
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=fixedincrement(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"])
                psychometric_function(feedback,value,response, None)
            else:
                case='3'
                feedback,value,response= fixedincrement_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"], path)
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=fixedincrement_vernier(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"])
                psychometric_function(feedback,value,response, None)
            else:
                case='5'
                feedback,value,response=fixedincrement_vernier_icatcher(case,selected_values["min_var"],selected_values["max_var"],selected_values["param1"],selected_values["param2"], path)

    elif selected_values["experiment"]=="Staircase":
        if selected_values["test"]=="Contrast Sensitivity":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='1'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='2'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
                psychometric_function(feedback,value,response, None)
            else:
                case='1'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"], path)
        elif selected_values["test"]=="Spatial Frequency":
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='3'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='4'
                feedback,value,response=staircase(case,selected_values["min_var"],selected_values["param1"])
                psychometric_function(feedback,value,response, None)
            else:
                case='3'
                feedback,value,response=staircase_icatcher(case,selected_values["min_var"],selected_values["param1"], path)
        else:
            if selected_values["eye_tracker"]=="Eye Tracker":
                if selected_values["hemisphere"]== "Two Hemispheres":
                    case='5'
                elif selected_values["hemisphere"]== "Four Hemispheres":
                    case='6'
                feedback,value,response=staircase_vernier(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"])
                psychometric_function(feedback,value,response, None)
            else:
                case='5'
                feedback,value,response=staircase_vernier_icatcher(case,selected_values["min_var"],selected_values["param1"],selected_values["param2"], path)
    sys.exit()

if __name__ == "__main__":
    main()
    sys.exit()
