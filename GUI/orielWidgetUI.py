# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'orielWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_orielForm(object):
    def setupUi(self, orielForm):
        orielForm.setObjectName("orielForm")
        orielForm.resize(350, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(orielForm.sizePolicy().hasHeightForWidth())
        orielForm.setSizePolicy(sizePolicy)
        orielForm.setMinimumSize(QtCore.QSize(350, 0))
        self.gridLayout_3 = QtWidgets.QGridLayout(orielForm)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.connectBtn = QtWidgets.QPushButton(orielForm)
        self.connectBtn.setMinimumSize(QtCore.QSize(120, 48))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectBtn.setIcon(icon)
        self.connectBtn.setIconSize(QtCore.QSize(32, 32))
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout_3.addWidget(self.connectBtn, 0, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_3.addWidget(self.statusLabel, 0, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.waveBtn = QtWidgets.QPushButton(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.waveBtn.setFont(font)
        self.waveBtn.setObjectName("waveBtn")
        self.gridLayout.addWidget(self.waveBtn, 2, 0, 1, 3)
        self.nmRadioBtn = QtWidgets.QRadioButton(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nmRadioBtn.setFont(font)
        self.nmRadioBtn.setChecked(True)
        self.nmRadioBtn.setObjectName("nmRadioBtn")
        self.gridLayout.addWidget(self.nmRadioBtn, 0, 1, 1, 1)
        self.entryBox = QtWidgets.QDoubleSpinBox(orielForm)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.entryBox.setFont(font)
        self.entryBox.setMaximum(1200.0)
        self.entryBox.setObjectName("entryBox")
        self.gridLayout.addWidget(self.entryBox, 0, 0, 2, 1)
        self.evRadioBtn = QtWidgets.QRadioButton(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.evRadioBtn.setFont(font)
        self.evRadioBtn.setObjectName("evRadioBtn")
        self.gridLayout.addWidget(self.evRadioBtn, 1, 1, 1, 1)
        self.goBtn = QtWidgets.QPushButton(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBtn.setIcon(icon1)
        self.goBtn.setIconSize(QtCore.QSize(64, 64))
        self.goBtn.setObjectName("goBtn")
        self.gridLayout.addWidget(self.goBtn, 0, 2, 2, 1)
        self.waveLabel = QtWidgets.QLabel(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.waveLabel.setFont(font)
        self.waveLabel.setObjectName("waveLabel")
        self.gridLayout.addWidget(self.waveLabel, 3, 0, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.responsesField = QtWidgets.QPlainTextEdit(orielForm)
        self.responsesField.setObjectName("responsesField")
        self.gridLayout_3.addWidget(self.responsesField, 4, 0, 1, 3)
        self.plainCmdBox = QtWidgets.QLineEdit(orielForm)
        self.plainCmdBox.setObjectName("plainCmdBox")
        self.gridLayout_3.addWidget(self.plainCmdBox, 5, 0, 1, 2)
        self.sendCmdBtn = QtWidgets.QPushButton(orielForm)
        self.sendCmdBtn.setObjectName("sendCmdBtn")
        self.gridLayout_3.addWidget(self.sendCmdBtn, 5, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.shutterCheckBtn = QtWidgets.QPushButton(orielForm)
        self.shutterCheckBtn.setObjectName("shutterCheckBtn")
        self.gridLayout_2.addWidget(self.shutterCheckBtn, 3, 2, 1, 1)
        self.shutterToggleBtn = QtWidgets.QPushButton(orielForm)
        self.shutterToggleBtn.setObjectName("shutterToggleBtn")
        self.gridLayout_2.addWidget(self.shutterToggleBtn, 3, 0, 1, 1)
        self.shutterStatusLabel = QtWidgets.QLabel(orielForm)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shutterStatusLabel.setFont(font)
        self.shutterStatusLabel.setObjectName("shutterStatusLabel")
        self.gridLayout_2.addWidget(self.shutterStatusLabel, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 3)

        self.retranslateUi(orielForm)
        QtCore.QMetaObject.connectSlotsByName(orielForm)

    def retranslateUi(self, orielForm):
        _translate = QtCore.QCoreApplication.translate
        orielForm.setWindowTitle(_translate("orielForm", "Form"))
        self.connectBtn.setText(_translate("orielForm", "Connect"))
        self.statusLabel.setText(_translate("orielForm", "Not connected"))
        self.waveBtn.setText(_translate("orielForm", "Wave?"))
        self.nmRadioBtn.setText(_translate("orielForm", "nm"))
        self.evRadioBtn.setText(_translate("orielForm", "eV"))
        self.goBtn.setText(_translate("orielForm", "Go"))
        self.waveLabel.setText(_translate("orielForm", "Current wave [nm]: (not set)"))
        self.label_3.setText(_translate("orielForm", "Responses"))
        self.plainCmdBox.setPlaceholderText(_translate("orielForm", "Plain command"))
        self.sendCmdBtn.setText(_translate("orielForm", "Send"))
        self.label.setText(_translate("orielForm", "Shutter:"))
        self.shutterCheckBtn.setText(_translate("orielForm", "Check?"))
        self.shutterToggleBtn.setText(_translate("orielForm", "Open/Close"))
        self.shutterStatusLabel.setText(_translate("orielForm", "?"))