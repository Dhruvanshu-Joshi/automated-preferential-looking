# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import parse_requirements

dependencies = parse_requirements.parse_requirements('requirements.txt')

hidden_imports = [
    'psychopy.locale_setup',
    'psychopy.prefs',
    'psychopy.gui',
    'psychopy.visual',
    'psychopy.core',
    'psychopy.data',
    'psychopy.event',
    'psychopy.logging',
    'psychopy.clock',
    'psychopy.colors',
    'psychopy.layout',
    'psychopy.constants',
    'psychopy.sound',
    'psychopy.hardware.keyboard',
    'numpy',
    'matplotlib.pyplot',
    'PIL.Image',
    'cv2',
    'PyQt6.QtWidgets',
    'torch',
    'platform',
    'pooch',
    # Add any other necessary hidden imports here
]

a = Analysis(
    ['src/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('PyQT_screens/*.png', 'PyQT_screens'),
        # Include any other necessary data files or folders here
    ],
    hiddenimports=dependencies + hidden_imports,
    hookspath=['.'],  # Ensure this path points to the directory with the hook file
    runtime_hooks=[],
    excludes=['PyQt5'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)
