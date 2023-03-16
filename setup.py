from setuptools import setup

APP = ['GUI.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Delim',
        'CFBundleDisplayName': 'Delim',
        'CFBundleIdentifier': 'com.example.Delim',
        'CFBundleVersion': '0.1',
        'CFBundleShortVersionString': '0.1.0',
    },
    'packages': ['os', 'tkinter', 'filedialog'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
