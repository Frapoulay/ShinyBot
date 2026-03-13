import sys
from unittest.mock import MagicMock

MOCK_MODULES = [
    "PyQt5",
    "PyQt5.QtWidgets",
    "PyQt5.QtGui",
    "PyQt5.QtCore",
    "cv2",
    "numpy",
    "win32api",
    "win32gui",
    "win32ui",
    "win32con",
    "win32process",
    "pygetwindow",
]

for module in MOCK_MODULES:
    sys.modules[module] = MagicMock()