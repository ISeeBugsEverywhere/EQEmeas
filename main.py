#!/usr/bin/python3
from GUI.EQEGUI import Ui_eqeWindow
from PyQt5 import QtWidgets, QtCore, QtGui
import sys, os
import numpy as np

class MainEqeApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_eqeWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    w = MainEqeApplication()
    w.show()
    sys.exit(app.exec())