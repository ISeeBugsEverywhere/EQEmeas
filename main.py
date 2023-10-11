#!/usr/bin/python3
from GUI.EQEGUI import Ui_eqeWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from HW.Oriel.OrielCS260USB import Oriel
import time, math

WAVE_LABEL_TEXT = "Current wave [nm]: {}"
import sys, os
import numpy as np

class MainEqeApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_eqeWindow()
        self.ui.setupUi(self)
        self.signals()
        self.oriel = Oriel()

    def signals(self):
        self.ui.connectBtnOriel.clicked.connect(self.connect_fn)
        self.ui.goBtn.clicked.connect(self.go_fn)
        self.ui.shutterToggleBtn.clicked.connect(self.toggle_fn)
        self.ui.shutterCheckBtn.clicked.connect(self.check_fn)
        self.ui.waveBtn.clicked.connect(self.wave_fn)
        self.ui.actionQuit.triggered.connect(self.quit_fn)

    def quit_fn(self):
        sys.exit(0)

    def connect_fn(self):
        r = self.oriel.setup()
        if r == 0:
            self.ui.statusLabel.setText("CONNECTED")
            cw = self.oriel.wave()
            self.ui.waveLabel.setText(WAVE_LABEL_TEXT.format(cw))
        elif r == 1:
            self.ui.responsesField.appendPlainText(f"NOT CONNECTED, status {r}")
        else:
            self.ui.responsesField.appendPlainText(f"STRANGE::{r}")
        pass

    def go_fn(self):
        c_wave = float(self.oriel.wave())
        val = self.ui.entryBox.value()
        unit = 'nm'  # default
        n_wave = 0
        if val < 179:
            unit = 'ev'
            self.ui.evRadioBtn.setChecked(True)
            self.ui.nmRadioBtn.setChecked(False)
            n_wave = 1239.75 / float(val)
        elif val > 180:
            unit = 'nm'
            self.ui.evRadioBtn.setChecked(False)
            self.ui.nmRadioBtn.setChecked(True)
            n_wave = val
        # if self.ui.nmRadioBtn.isChecked():
        #     unit = 'nm'
        # elif self.ui.evRadioBtn.isChecked():
        #     unit = 'ev'
        bts = self.oriel.gowave(val, unit)
        self.ui.responsesField.appendPlainText(f"Bytes written: {bts}")
        #     delay?
        time.sleep(math.floor(abs(c_wave - n_wave)) / 10.0 * 0.125)
        cw = self.oriel.wave()
        self.ui.waveLabel.setText(WAVE_LABEL_TEXT.format(cw))

    def toggle_fn(self):
        s = self.oriel.shutter()
        # self.ui.responsesField.appendPlainText(str(s)+"\n")
        if s.lower() == 'c':
            self.oriel.openShutter()
            self.ui.shutterStatusLabel.setText("OPENED")
        elif s.lower() == 'o':
            self.oriel.closeShutter()
            self.ui.shutterStatusLabel.setText("CLOSED")

    def check_fn(self):
        s = self.oriel.shutter()
        # self.ui.responsesField.appendPlainText(str(s) + "\n")
        if s.lower() == 'c':
            self.ui.responsesField.appendPlainText("Shutter is closed.")
        elif s.lower() == 'o':
            self.ui.responsesField.appendPlainText("Shutter is opened.")

    def wave_fn(self):
        w = self.oriel.wave()
        self.ui.waveLabel.setText(WAVE_LABEL_TEXT.format(w))
        self.ui.responsesField.appendPlainText(f"Current wave: {w}")


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    w = MainEqeApplication()
    w.show()
    sys.exit(app.exec())