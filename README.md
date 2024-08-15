

# APL: Automated Preferential Looking
<!-- TABLE OF CONTENTS -->
## :book: Table of Contents

1. [➤ About The Project](#pencil-about-the-project)
2. [➤ Prerequisites](#prerequisites)
3. [➤ Roadmap](#dart-roadmap)
4. [➤ Folder Structure](#cactus-folder-structure)
5. [➤ Implementation](#implementation)
6. [➤ Features](#features)
7. [➤ Future Goals](#future-goals)
8. [➤ Acknowledgments](#acknowledgments)

    <!-- <li><a href="#libraries-used"> ➤ Libraries Used</a></li>
    <li><a href="#roadmap"> ➤ Roadmap</a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#implementation"> ➤ Implementation</a></li>
    <li><a href="#feature"> ➤ Features</a></li>
    <li><a href="#future"> ➤ Future Goals</a></li>
    <li><a href="#acknowledgments"> ➤ Acknowledgments</a></li>
  <!-- </ol>


-----------------------------------------------------

<!-- <h2 id="about-the-project"> :pencil: About The project</h2> -->
## :pencil: About The project
This project is the work for the Google Summer of Code 2023, with the organisation INCF. The project is created by [Soham Mulye](https://github.com/Shazam213) under the mentoring of Suresh Krishna, PhD from McGill University.
This project aims to develop a ready-to-deploy application suite that will address the limitations of traditional preferential looking tests in infants by integrating hardware devices or deep learning-based infant eye trackers, and visual stimuli analysis into a user-friendly graphical user interface (GUI).


-----------------------------------------------------

<!-- PREREQUISITES -->
<!-- <h2 id="prerequisites"> Prerequisites</h2> -->
## Prerequisites
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) <br>


<!--This project is written in Python programming language. <br>-->
The following open source packages are used in this project:
* Numpy
* Matplotlib
* Scikit-Learn
* TensorFlow
* Keras
* PsychoPy
* OpenCV
* Tkinter

-----------------------------------------------------


<!-- ROADMAP -->
<!-- <h2 id="roadmap"> :dart: Roadmap</h2> -->
## :dart: Roadmap

The result of this work which was about 420 hours, is divided in the following parts:

1. Psychophysics Research and Experimentation:
    *   In-depth research into psychophysics, including the study of various psychophysical experiments and the underlying psychometric functions.Exploration and understanding of the theoretical aspects related to visual perception and responses. All the experiments were created using [PsychoPy](https://www.psychopy.org/)

2. Psychopy Experiment Development:

    * Design and implementation of psychophysical experiments using the Psychopy library. Creation of controlled experimental environments with systematic manipulation of visual stimuli, such as grating acuity and contrast sensitivity tests.

3. Eye Tracking Integration:
    * Seamless integration of an eye-tracking model into the developed experiments to enable automated gaze tracking Development of psychometric function to monitor and analyze infant gaze, eye movements, and responses to visual stimuli.

4. User-Friendly GUI and Program Integration:

    * Development of an intuitive and user-friendly graphical user interface (GUI) using Tkinter. Integration of all three components, including the visual stimuli experiments, eye-tracking functionality, and data analysis, into a cohesive Python program.
-----------------------------------------------------

<!-- :paw_prints:-->
<!-- FOLDER STRUCTURE -->
<!-- <h2 id="folder-structure"> :cactus: Folder Structure</h2> -->
## :cactus: Folder Structure  
        .
        └── automated-preferential-looking/
        ├── resources
        ├── src/
        │ ├── data
        │ ├── pycache
        │ ├── icatcher/
        │ ├── init.py
        │ ├── fixed_increment.py
        │ ├── fixed_increment_icatcher.py
        │ ├── gui.py
        │ ├── main.py
        │ ├── predict.py
        │ ├── psychometric_function.py
        │ ├── staircase.py
        │ └── staircase_icatcher.py
        ├── LICENSE
        ├── README.md
        └── requirements.txt
    

-----------------------------------------------------
<!-- :paw_prints:-->
<!-- IMPLEMENTATION -->
<!-- <h2 id="implementation"> Implementation</h2> -->
## Implementation

To execute the program on your system, please follow these steps.
* Clone the repository into your local system:
    ```sh
    git clone https://github.com/Shazam213/automated-preferential-looking.git
    ```

* Navigate to the cloned directory:
    ```sh
    cd automated-preferential-looking
    ```

* Download all the required packages:
    ```sh
    pip install -r requirements.txt
    ```
* Navigate to the src folder:
    ```sh
    cd src
    ```

* Now execute the program:
    ```sh
    python main.py
    ```
Ps- You might face errors while psychopy installations. You can refer this [link](https://github.com/Shazam213/automated-preferential-looking/tree/visual-stimuli#getting-started).

* When running for the first time the app may take some time to load all the packages and also to download the eye tracking model.

-----------------------------------------------------
<!-- :paw_prints:-->
<!-- FEATURE -->
<!-- <h2 id="feature"> Features</h2> -->
## Features
 
 1. Starting the Program you first get the easy to use GUI.
 ![GUI screen 1](./resources/gui_screen1.png)
 ![GUI screen 2](./resources/gui_screen2.png)
 ![GUI screen 3](./resources/gui_screen3.png)
 ![GUI screen 4](./resources/gui_screen4.png)
 2. Once you've chosen the particular experiment and configured the parameter values, the experiment commences. Here is the example of staircase pattern of spatial frequency experiment using eye tracking model
 ![Experiment start](./resources/experiment_start_screen.png)
 ![Stimuli](./resources/stimuli.png)
 3. Upon finishing the experiment, you'll see the psychometric function.
![Psychometric fucntion](./resources/psychometric_funct.png)
 4. Here's a look at the eye tracking model (iCatcher+) in operation.  Because the model was trained for infants and young children, its accuracy suffers when tested on adults:
[![iCatcher representatiion](resources\demo_icatcher_experiment.png)](https://youtu.be/AfOxSQmwGKM)
-----------------------------------------------------
<!-- FUTURE -->
<!-- <h2 id="future"> Future Goals </h2> -->
## Future Goals

Alas, the end of Summer of Code shouldn't be the end of this project! With an amazing scope to go forward, I would love to put much more effort and create a full-working application that could be used in a clinical setting with help and testing from other researchers and labs we already had contact with.The project has laid a strong foundation for efficient measurement of visual functions in infants and young children. Future work may include:

* Further refinement and optimization of the deep learning-based infant eye tracker model to improve accuracy.

* Collaborations with healthcare professionals and researchers to refine and validate the application's use in clinical settings.
* Deploy the program as a pip package or on a website.

Also due to the unavailibility of traditional eye tracking devices, eye tracker integration was not possible so instead for those experiments currently input is being taken through keyboard. But later it can also be implemented easily using the API developed by [Ioannis Valasakis](https://github.com/wizofe/ao-baby-tracker)

-----------------------------------------------------

<!-- Acknowledgments -->
<!-- <h2 id="acknowledgments"> Acknowledgments! </h2> -->
## Acknowledgments
I'd like to express my gratitude to my mentor, Dr. Suresh Krishna from McGill University, for providing invaluable insights and information throughout this project. While at times the information was quite complex, I understand that it will greatly benefit future iterations of the application and collaborative research with other scientists.

I would also like to extend my appreciation to the developers of [iCatcher+](https://github.com/icatcherplus/icatcher_plus), the eye-tracking model that has been seamlessly integrated into the program for gaze detection and test automation.

With the generous support of Google's open-source initiatives, I hope that I've sown the seeds of a useful program and provided valuable code suggestions. These contributions have the potential to make a significant impact in clinical settings in the future. Thank you, Google!

```
automated-preferential-looking
├─ LICENSE
├─ New folder
├─ PyQT_screens
│  ├─ button1.png
│  ├─ button2.png
│  ├─ eye1.png
│  ├─ eye2.png
│  ├─ eye3.png
│  ├─ image.png
│  ├─ index.py
│  ├─ load.png
│  ├─ main - Copy.py
│  ├─ main.py
│  ├─ panda - Copy.png
│  ├─ panda.png
│  ├─ panda2.png
│  ├─ panda3.png
│  ├─ panda4.png
│  ├─ panda5.png
│  ├─ panda6.png
│  ├─ panda7.png
│  ├─ panda8.png
│  ├─ screen2.py
│  ├─ screen3.py
│  ├─ screen4.py
│  ├─ screen5.py
│  ├─ screen6.py
│  ├─ screen7.py
│  ├─ screen8.py
│  ├─ start.png
│  ├─ stimulus.png
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ index.cpython-311.pyc
│     ├─ main.cpython-311.pyc
│     ├─ screen2.cpython-311.pyc
│     ├─ screen3.cpython-311.pyc
│     ├─ screen4.cpython-311.pyc
│     ├─ screen5.cpython-311.pyc
│     ├─ screen6.cpython-311.pyc
│     ├─ screen7.cpython-311.pyc
│     ├─ screen8.cpython-311.pyc
│     └─ __init__.cpython-311.pyc
├─ README.md
├─ requirements.txt
├─ resources
│  ├─ demo.mp4
│  ├─ demo_icatcher_experiment.png
│  ├─ experiment_start_screen.png
│  ├─ gui_screen1.png
│  ├─ gui_screen2.png
│  ├─ gui_screen3.png
│  ├─ gui_screen4.png
│  ├─ icatcher_demo.mp4
│  ├─ icatcher_demo_thumbnail.png
│  ├─ psychometric_funct.png
│  └─ stimuli.png
├─ screens
│  └─ demo.ui
└─ src
   ├─ back_up
   │  ├─ main.exe
   │  └─ main.spec
   ├─ build
   │  └─ main
   │     ├─ Analysis-00.toc
   │     ├─ base_library.zip
   │     ├─ EXE-00.toc
   │     ├─ localpycs
   │     │  ├─ pyimod01_archive.pyc
   │     │  ├─ pyimod02_importers.pyc
   │     │  ├─ pyimod03_ctypes.pyc
   │     │  ├─ pyimod04_pywin32.pyc
   │     │  └─ struct.pyc
   │     ├─ main.pkg
   │     ├─ PKG-00.toc
   │     ├─ PYZ-00.pyz
   │     ├─ PYZ-00.toc
   │     ├─ Tree-00.toc
   │     ├─ Tree-01.toc
   │     ├─ Tree-02.toc
   │     ├─ warn-main.txt
   │     └─ xref-main.html
   ├─ data
   │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.csv
   │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.log
   │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.psydat
   │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.csv
   │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.log
   │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.psydat
   │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.csv
   │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.log
   │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.psydat
   │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.csv
   │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.log
   │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.psydat
   │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.csv
   │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.log
   │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.psydat
   │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.csv
   │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.log
   │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.psydat
   │  ├─ 221852_stimuli3_2024-06-06_21h50.02.125.log
   │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.csv
   │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.log
   │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.psydat
   │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.csv
   │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.log
   │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.psydat
   │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.avi
   │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.csv
   │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.log
   │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.psydat
   │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.csv
   │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.log
   │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.psydat
   │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.csv
   │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.log
   │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.psydat
   │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.csv
   │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.log
   │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.psydat
   │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.avi
   │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.csv
   │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.log
   │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.psydat
   │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.avi
   │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.csv
   │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.log
   │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.psydat
   │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.avi
   │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.csv
   │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.log
   │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.psydat
   │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.csv
   │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.log
   │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.psydat
   │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.csv
   │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.log
   │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.psydat
   │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.csv
   │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.log
   │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.psydat
   │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.csv
   │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.log
   │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.psydat
   │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.avi
   │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.csv
   │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.log
   │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.psydat
   │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.csv
   │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.log
   │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.psydat
   │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.csv
   │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.log
   │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.psydat
   │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.csv
   │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.log
   │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.psydat
   │  ├─ 834211_stimuli3_2024-06-08_17h24.09.063.log
   │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.csv
   │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.log
   │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.psydat
   │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.csv
   │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.log
   │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.psydat
   │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.csv
   │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.log
   │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.psydat
   │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.csv
   │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.log
   │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.psydat
   │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.csv
   │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.log
   │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.psydat
   │  ├─ 974578_stimuli3_2024-06-08_13h32.15.131.csv
   │  ├─ 974578_stimuli3_2024-06-08_13h32.15.131.log
   │  └─ 974578_stimuli3_2024-06-08_13h32.15.131.psydat
   ├─ dist
   │  └─ main.exe
   ├─ fixed_increment.py
   ├─ fixed_increment_icatcher.py
   ├─ gui.py
   ├─ icatcher
   │  ├─ cli.py
   │  ├─ draw.py
   │  ├─ models.py
   │  ├─ options.py
   │  ├─ parsers.py
   │  ├─ video.py
   │  ├─ __init__.py
   │  └─ __pycache__
   │     ├─ cli.cpython-311.pyc
   │     ├─ draw.cpython-311.pyc
   │     ├─ models.cpython-311.pyc
   │     ├─ options.cpython-311.pyc
   │     ├─ parsers.cpython-311.pyc
   │     ├─ video.cpython-311.pyc
   │     └─ __init__.cpython-311.pyc
   ├─ main.py
   ├─ main.spec
   ├─ predict.py
   ├─ psychometric_function.py
   ├─ screen6.py
   ├─ staircase.py
   ├─ staircase_icatcher.py
   ├─ __init__.py
   └─ __pycache__
      ├─ fixed_increment.cpython-311.pyc
      ├─ fixed_increment_icatcher.cpython-311.pyc
      ├─ gui.cpython-311.pyc
      ├─ predict.cpython-311.pyc
      ├─ psychometric_function.cpython-311.pyc
      ├─ staircase.cpython-311.pyc
      └─ staircase_icatcher.cpython-311.pyc

```
```
automated-preferential-looking
├─ build
│  └─ main
│     ├─ Analysis-00.toc
│     ├─ base_library.zip
│     ├─ COLLECT-00.toc
│     ├─ EXE-00.toc
│     ├─ localpycs
│     │  ├─ pyimod01_archive.pyc
│     │  ├─ pyimod02_importers.pyc
│     │  ├─ pyimod03_ctypes.pyc
│     │  ├─ pyimod04_pywin32.pyc
│     │  └─ struct.pyc
│     ├─ main.pkg
│     ├─ PKG-00.toc
│     ├─ PYZ-00.pyz
│     ├─ PYZ-00.toc
│     ├─ Tree-00.toc
│     ├─ Tree-01.toc
│     ├─ Tree-02.toc
│     ├─ warn-main.txt
│     └─ xref-main.html
├─ dist
│  └─ main.exe
├─ freetype.dll
├─ freetype.lib
├─ gather_hidden_imports.py
├─ hidden_imports.txt
├─ hook-psychopy.iohub.py
├─ LICENSE
├─ main.spec
├─ New folder
│  └─ main.exe
├─ parse_requirements.py
├─ PyQT_screens
│  ├─ button1.png
│  ├─ button2.png
│  ├─ eye1.png
│  ├─ eye2.png
│  ├─ eye3.png
│  ├─ image.png
│  ├─ index.py
│  ├─ load.png
│  ├─ main - Copy.py
│  ├─ main.py
│  ├─ panda - Copy.png
│  ├─ panda.png
│  ├─ panda2.png
│  ├─ panda3.png
│  ├─ panda4.png
│  ├─ panda5.png
│  ├─ panda6.png
│  ├─ panda7.png
│  ├─ panda8.png
│  ├─ screen2.py
│  ├─ screen3.py
│  ├─ screen4.py
│  ├─ screen5.py
│  ├─ screen6.py
│  ├─ screen7.py
│  ├─ screen8.py
│  ├─ start.png
│  ├─ stimulus.png
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ index.cpython-311.pyc
│     ├─ main.cpython-311.pyc
│     ├─ screen2.cpython-311.pyc
│     ├─ screen3.cpython-311.pyc
│     ├─ screen4.cpython-311.pyc
│     ├─ screen5.cpython-311.pyc
│     ├─ screen6.cpython-311.pyc
│     ├─ screen7.cpython-311.pyc
│     ├─ screen8.cpython-311.pyc
│     └─ __init__.cpython-311.pyc
├─ README.md
├─ requirements.txt
├─ resources
│  ├─ demo.mp4
│  ├─ demo_icatcher_experiment.png
│  ├─ experiment_start_screen.png
│  ├─ gui_screen1.png
│  ├─ gui_screen2.png
│  ├─ gui_screen3.png
│  ├─ gui_screen4.png
│  ├─ icatcher_demo.mp4
│  ├─ icatcher_demo_thumbnail.png
│  ├─ psychometric_funct.png
│  └─ stimuli.png
├─ screens
│  └─ demo.ui
├─ src
│  ├─ back_up
│  │  ├─ main.exe
│  │  └─ main.spec
│  ├─ build
│  │  └─ main
│  │     ├─ Analysis-00.toc
│  │     ├─ base_library.zip
│  │     ├─ EXE-00.toc
│  │     ├─ localpycs
│  │     │  ├─ pyimod01_archive.pyc
│  │     │  ├─ pyimod02_importers.pyc
│  │     │  ├─ pyimod03_ctypes.pyc
│  │     │  ├─ pyimod04_pywin32.pyc
│  │     │  └─ struct.pyc
│  │     ├─ main.pkg
│  │     ├─ PKG-00.toc
│  │     ├─ PYZ-00.pyz
│  │     ├─ PYZ-00.toc
│  │     ├─ Tree-00.toc
│  │     ├─ Tree-01.toc
│  │     ├─ Tree-02.toc
│  │     ├─ warn-main.txt
│  │     └─ xref-main.html
│  ├─ data
│  │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.csv
│  │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.log
│  │  ├─ 001821_stimuli3_2024-06-08_13h07.01.241.psydat
│  │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.csv
│  │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.log
│  │  ├─ 026522_stimuli3_2024-06-08_15h07.51.341.psydat
│  │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.csv
│  │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.log
│  │  ├─ 072292_stimuli3_2024-06-08_17h17.14.517.psydat
│  │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.csv
│  │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.log
│  │  ├─ 099024_stimuli4_2024-06-29_11h38.40.654.psydat
│  │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.csv
│  │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.log
│  │  ├─ 103717_stimuli3_2024-06-08_15h05.19.946.psydat
│  │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.csv
│  │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.log
│  │  ├─ 205897_stimuli3_2024-06-08_13h35.14.746.psydat
│  │  ├─ 221852_stimuli3_2024-06-06_21h50.02.125.log
│  │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.csv
│  │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.log
│  │  ├─ 267152_stimuli3_2024-06-08_17h27.11.685.psydat
│  │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.csv
│  │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.log
│  │  ├─ 294732_stimuli4_2024-06-29_11h36.51.788.psydat
│  │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.avi
│  │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.csv
│  │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.log
│  │  ├─ 316896_stimuli3_2024-06-08_13h02.14.287.psydat
│  │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.csv
│  │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.log
│  │  ├─ 356607_stimuli4_2024-06-29_12h57.29.336.psydat
│  │  ├─ 369055_stimuli3_2024-06-30_18h21.21.916.csv
│  │  ├─ 369055_stimuli3_2024-06-30_18h21.21.916.log
│  │  ├─ 369055_stimuli3_2024-06-30_18h21.21.916.psydat
│  │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.csv
│  │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.log
│  │  ├─ 383395_stimuli3_2024-06-08_13h06.15.793.psydat
│  │  ├─ 469203_stimuli3_2024-06-30_18h40.00.251.csv
│  │  ├─ 469203_stimuli3_2024-06-30_18h40.00.251.log
│  │  ├─ 469203_stimuli3_2024-06-30_18h40.00.251.psydat
│  │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.csv
│  │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.log
│  │  ├─ 515877_stimuli4_2024-06-29_13h34.17.829.psydat
│  │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.avi
│  │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.csv
│  │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.log
│  │  ├─ 546589_stimuli3_2024-06-08_17h30.22.899.psydat
│  │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.avi
│  │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.csv
│  │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.log
│  │  ├─ 586370_stimuli3_2024-06-08_17h35.12.136.psydat
│  │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.avi
│  │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.csv
│  │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.log
│  │  ├─ 644858_stimuli4_2024-06-29_13h10.38.112.psydat
│  │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.csv
│  │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.log
│  │  ├─ 679703_stimuli3_2024-06-08_13h38.07.417.psydat
│  │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.csv
│  │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.log
│  │  ├─ 717893_stimuli3_2024-06-08_12h48.30.145.psydat
│  │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.csv
│  │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.log
│  │  ├─ 728382_stimuli3_2024-06-08_13h05.02.387.psydat
│  │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.csv
│  │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.log
│  │  ├─ 738229_stimuli4_2024-06-29_11h40.44.628.psydat
│  │  ├─ 777666_stimuli4_2024-06-29_20h32.35.147.csv
│  │  ├─ 777666_stimuli4_2024-06-29_20h32.35.147.log
│  │  ├─ 777666_stimuli4_2024-06-29_20h32.35.147.psydat
│  │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.avi
│  │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.csv
│  │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.log
│  │  ├─ 779996_stimuli3_2024-06-29_13h46.45.232.psydat
│  │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.csv
│  │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.log
│  │  ├─ 820626_stimuli4_2024-06-29_00h45.46.019.psydat
│  │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.csv
│  │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.log
│  │  ├─ 827809_stimuli4_2024-06-29_12h56.15.501.psydat
│  │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.csv
│  │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.log
│  │  ├─ 833417_stimuli4_2024-06-29_12h39.52.059.psydat
│  │  ├─ 834211_stimuli3_2024-06-08_17h24.09.063.log
│  │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.csv
│  │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.log
│  │  ├─ 843110_stimuli3_2024-06-08_13h33.31.996.psydat
│  │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.csv
│  │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.log
│  │  ├─ 854668_stimuli4_2024-06-28_20h24.29.208.psydat
│  │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.csv
│  │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.log
│  │  ├─ 865892_stimuli3_2024-06-06_21h48.52.415.psydat
│  │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.csv
│  │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.log
│  │  ├─ 907768_stimuli4_2024-06-29_12h46.27.568.psydat
│  │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.csv
│  │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.log
│  │  ├─ 962172_stimuli4_2024-06-29_11h37.47.670.psydat
│  │  ├─ 974578_stimuli3_2024-06-08_13h32.15.131.csv
│  │  ├─ 974578_stimuli3_2024-06-08_13h32.15.131.log
│  │  ├─ 974578_stimuli3_2024-06-08_13h32.15.131.psydat
│  │  ├─ 982771_stimuli3_2024-06-30_18h32.31.453.csv
│  │  ├─ 982771_stimuli3_2024-06-30_18h32.31.453.log
│  │  └─ 982771_stimuli3_2024-06-30_18h32.31.453.psydat
│  ├─ dist
│  │  └─ main.exe
│  ├─ fixed_increment.py
│  ├─ fixed_increment_icatcher.py
│  ├─ gather_hidden_imports.py
│  ├─ gui.py
│  ├─ icatcher
│  │  ├─ cli.py
│  │  ├─ draw.py
│  │  ├─ models.py
│  │  ├─ options.py
│  │  ├─ parsers.py
│  │  ├─ video.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ cli.cpython-311.pyc
│  │     ├─ draw.cpython-311.pyc
│  │     ├─ models.cpython-311.pyc
│  │     ├─ options.cpython-311.pyc
│  │     ├─ parsers.cpython-311.pyc
│  │     ├─ video.cpython-311.pyc
│  │     └─ __init__.cpython-311.pyc
│  ├─ main.py
│  ├─ predict.py
│  ├─ psychometric_function.py
│  ├─ screen6.py
│  ├─ staircase.py
│  ├─ staircase_icatcher.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ fixed_increment.cpython-311.pyc
│     ├─ fixed_increment_icatcher.cpython-311.pyc
│     ├─ gui.cpython-311.pyc
│     ├─ predict.cpython-311.pyc
│     ├─ psychometric_function.cpython-311.pyc
│     ├─ staircase.cpython-311.pyc
│     └─ staircase_icatcher.cpython-311.pyc
└─ __pycache__
   ├─ hook-psychopy.iohub.cpython-311.pyc
   └─ parse_requirements.cpython-311.pyc

```