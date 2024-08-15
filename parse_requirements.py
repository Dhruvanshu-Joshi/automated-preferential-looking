# parse_requirements.py
import re

def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    dependencies = []
    for line in lines:
        line = re.sub(r'#.*', '', line).strip()
        if line:
            if '==' in line:
                package = line.split('==')[0]
            elif '>=' in line:
                package = line.split('>=')[0]
            elif '<=' in line:
                package = line.split('<=')[0]
            elif '>' in line:
                package = line.split('>')[0]
            elif '<' in line:
                package = line.split('<')[0]
            else:
                package = line
            module = package_to_module(package)
            if module:
                dependencies.append(module)
    return dependencies

def package_to_module(package):
    # Convert package names to module names
    package_module_mapping = {
        'opencv-python': 'cv2',
        # Add more mappings as needed
        'ffmpeg-python': '',
        'batch-face': 'batch_face',
    }
    return package_module_mapping.get(package, package)
