#!/usr/bin/python3

from GUI.EQEGUI import Ui_eqeWindow
from PyQt5 import QtWidgets, QtGui
from HW.OrielHWCS260.OrielCS260USB import Oriel
from GUI.OrielWidget import OrielControlWidget
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
import sys


class MainEqeApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_eqeWindow()
        self.ui.setupUi(self)
        self.ow = None
        self.oriel = Oriel()
        self.load_oriel_widget()
        self.signals()
        self.load_image(0) # at start - no problems?
        self.oriel_status()
        self.sourcemeter_status()

    def load_oriel_widget(self):
        self.ow = OrielControlWidget()
        lay = self.ui.orielTab.layout()
        lay.addWidget(self.ow)
        self.ow.show()
        self.ow.setOriel(self.oriel)
        pass


    def signals(self):
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
            self.ow.ui.statusLabel.setText("CONNECTED")
            cw = self.oriel.wave()
            self.ow.ui.waveLabel.setText(WAVE_LABEL_TEXT.format(cw))
            self.ow.ui.responsesField.appendPlainText(f"CONNECTED, status {r}")
            return r
        elif r == 1:
            self.ow.ui.responsesField.appendPlainText(f"NOT CONNECTED, status {r}")
            return r
        else:
            self.ow.ui.responsesField.appendPlainText(f"STRANGE::{r}")
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


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    w = MainEqeApplication()
    w.show()
    sys.exit(app.exec())