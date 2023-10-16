#!/usr/bin/python3
import Qt

from GUI.EQEGUI import Ui_eqeWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from HW.Oriel.OrielCS260USB import Oriel
import time, math

WAVE_LABEL_TEXT = "Current wave [nm]: {}"
OK_PIC = "GUI/Icons/security-high.png"
BAD_PIC = "GUI/Icons/security-low.png"
STRANGE_PIC = "GUI/Icons/security-medium.png"
ORIEL_OK = "GUI/Icons/oriel_ok.png"
ORIEL_NO = "GUI/Icons/oriel_no.png"
ORIEL_Q = "GUI/Icons/oriel_q.png"
K_OK = "GUI/Icons/k_ok.png"
K_Q = "GUI/Icons/k_q.png"
K_NO = "GUI/Icons/k_no.png"
import sys, os
import numpy as np

class MainEqeApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_eqeWindow()
        self.ui.setupUi(self)
        self.signals()
        self.oriel = Oriel()
        self.load_image(0) # at start - no problems?
        self.oriel_status()
        self.sourcemeter_status()


    def signals(self):
        self.ui.connectBtnOriel.clicked.connect(self.connect_fn)
        self.ui.goBtn.clicked.connect(self.go_fn)
        self.ui.shutterToggleBtn.clicked.connect(self.toggle_fn)
        self.ui.shutterCheckBtn.clicked.connect(self.check_fn)
        self.ui.waveBtn.clicked.connect(self.wave_fn)
        self.ui.actionQuit.triggered.connect(self.quit_fn)
        self.ui.connectBtn.clicked.connect(self.connect_all)

    def quit_fn(self):
        sys.exit(0)

    def oriel_status(self, r=-1):
        if r == 0:
            qImage = QtGui.QImage(ORIEL_OK)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.oriel_status.setPixmap(pixmap)
            self.ui.oriel_status.setScaledContents(True)
        elif r == 1:
            qImage = QtGui.QImage(ORIEL_NO)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.oriel_status.setPixmap(pixmap)
            self.ui.oriel_status.setScaledContents(True)
        else:
            qImage = QtGui.QImage(ORIEL_Q)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.oriel_status.setPixmap(pixmap)
            self.ui.oriel_status.setScaledContents(True)

    def sourcemeter_status(self, r = -1):
        if r == 0:
            qImage = QtGui.QImage(K_OK)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.device_status.setPixmap(pixmap)
            self.ui.device_status.setScaledContents(True)
        elif r == 1:
            qImage = QtGui.QImage(K_NO)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.device_status.setPixmap(pixmap)
            self.ui.device_status.setScaledContents(True)
        else:
            qImage = QtGui.QImage(K_Q)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.device_status.setPixmap(pixmap)
            self.ui.device_status.setScaledContents(True)

    def connect_fn(self):
        """
        connects oriel monochromator
        :return: 0 - ok, 1 - no oriel
        """
        r = self.oriel.setup()
        if r == 0:
            self.ui.statusLabel.setText("CONNECTED")
            cw = self.oriel.wave()
            self.ui.waveLabel.setText(WAVE_LABEL_TEXT.format(cw))
            self.ui.responsesField.appendPlainText(f"CONNECTED, status {r}")
            return r
        elif r == 1:
            self.ui.responsesField.appendPlainText(f"NOT CONNECTED, status {r}")
            return r
        else:
            self.ui.responsesField.appendPlainText(f"STRANGE::{r}")
            return r
        pass

    def connect_all(self):
        oriel_status = self.connect_fn()
        self.load_image(oriel_status)
        self.oriel_status(oriel_status)
        pass

    def load_image(self, status):
        if status == 0:
            qImage = QtGui.QImage(OK_PIC)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.statusPictureView.setPixmap(pixmap)
            self.ui.statusPictureView.setScaledContents(True)
        elif status == 1:
            qImage = QtGui.QImage(BAD_PIC)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.statusPictureView.setPixmap(pixmap)
            self.ui.statusPictureView.setScaledContents(True)
        else:
            qImage = QtGui.QImage(STRANGE_PIC)
            pixmap = QtGui.QPixmap.fromImage(qImage)
            self.ui.statusPictureView.setPixmap(pixmap)
            self.ui.statusPictureView.setScaledContents(True)



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