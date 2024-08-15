from distutils.core import setup
import py2exe
import os
import sys

# Append the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# The name of your .py file
progName = 'src\\main.py'

# Initialize Holder Files
data_files = []

# Function to add files to data_files
def add_files_to_data_files(directory, target_dir):
    files = []
    for root, dirs, filenames in os.walk(directory):
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')  # Skip __pycache__ directories
        for filename in filenames:
            files.append(os.path.join(root, filename))
    data_files.append((target_dir, files))

# Add Psychopy preferences files
add_files_to_data_files('C:\\Users\\jmahe\\AppData\\Roaming\\Python\\Python311\\site-packages\\psychopy\\preferences', 'psychopy\\preferences')

# Add PyQT_screens files
add_files_to_data_files('PyQT_screens', 'PyQT_screens')

# Add src files
add_files_to_data_files('src', 'src')

# Add matplotlib data files
add_files_to_data_files('C:\\Users\\jmahe\\AppData\\Roaming\\Python\\Python311\\site-packages\\matplotlib\\mpl-data', 'matplotlib\\mpl-data')

# Define the setup
setup(
    console=[progName],
    data_files=data_files,
    options={
        "py2exe": {
            "skip_archive": True,
            "optimize": 2,
            "includes": [
                "fixed_increment",
                "staircase",
                "fixed_increment_icatcher",
                "staircase_icatcher",
                "psychometric_function",
                "PyQT_screens.main",
                "PyQt6"
            ],
            "excludes": [
                "tkinter",
                "unittest",
                "email",
                "html",
                "http",
                "xml",
                "pydoc",
                "pdb",
                "doctest",
                "optparse",
                "pickle",
                "platform"
            ],
        }
    }
)
