# hook-psychopy.iohub.py

from PyInstaller.utils.hooks import collect_submodules

hiddenimports = collect_submodules('psychopy.iohub')
