import sys
from cx_Freeze import setup, Executable

setup(
    name='MyApp',
    version='0.1',
    description='Description',
    executables = [
        Executable('simplehttpd.py', base='Win32GUI' if sys.platform == 'win32' else None)
    ],
)



