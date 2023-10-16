# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EQEGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_eqeWindow(object):
    def setupUi(self, eqeWindow):
        eqeWindow.setObjectName("eqeWindow")
        eqeWindow.resize(1006, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(eqeWindow.sizePolicy().hasHeightForWidth())
        eqeWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/spectrum.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eqeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(eqeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.orielWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orielWidget.sizePolicy().hasHeightForWidth())
        self.orielWidget.setSizePolicy(sizePolicy)
        self.orielWidget.setObjectName("orielWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.connectBtnOriel = QtWidgets.QPushButton(self.tab_4)
        self.connectBtnOriel.setMinimumSize(QtCore.QSize(120, 48))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectBtnOriel.setIcon(icon1)
        self.connectBtnOriel.setIconSize(QtCore.QSize(32, 32))
        self.connectBtnOriel.setObjectName("connectBtnOriel")
        self.gridLayout_7.addWidget(self.connectBtnOriel, 0, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_7.addWidget(self.statusLabel, 0, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.waveBtn = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.waveBtn.setFont(font)
        self.waveBtn.setObjectName("waveBtn")
        self.gridLayout_6.addWidget(self.waveBtn, 2, 0, 1, 3)
        self.nmRadioBtn = QtWidgets.QRadioButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.nmRadioBtn.setFont(font)
        self.nmRadioBtn.setChecked(True)
        self.nmRadioBtn.setObjectName("nmRadioBtn")
        self.gridLayout_6.addWidget(self.nmRadioBtn, 0, 1, 1, 1)
        self.entryBox = QtWidgets.QDoubleSpinBox(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.entryBox.setFont(font)
        self.entryBox.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.entryBox.setMaximum(1200.0)
        self.entryBox.setObjectName("entryBox")
        self.gridLayout_6.addWidget(self.entryBox, 0, 0, 2, 1)
        self.evRadioBtn = QtWidgets.QRadioButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.evRadioBtn.setFont(font)
        self.evRadioBtn.setObjectName("evRadioBtn")
        self.gridLayout_6.addWidget(self.evRadioBtn, 1, 1, 1, 1)
        self.goBtn = QtWidgets.QPushButton(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.goBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBtn.setIcon(icon2)
        self.goBtn.setIconSize(QtCore.QSize(64, 64))
        self.goBtn.setObjectName("goBtn")
        self.gridLayout_6.addWidget(self.goBtn, 0, 2, 2, 1)
        self.waveLabel = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.waveLabel.setFont(font)
        self.waveLabel.setObjectName("waveLabel")
        self.gridLayout_6.addWidget(self.waveLabel, 3, 0, 1, 3)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.shutterStatusLabel = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.shutterStatusLabel.setFont(font)
        self.shutterStatusLabel.setObjectName("shutterStatusLabel")
        self.gridLayout_5.addWidget(self.shutterStatusLabel, 2, 2, 1, 1)
        self.shutterToggleBtn = QtWidgets.QPushButton(self.tab_4)
        self.shutterToggleBtn.setObjectName("shutterToggleBtn")
        self.gridLayout_5.addWidget(self.shutterToggleBtn, 3, 0, 1, 1)
        self.shutterCheckBtn = QtWidgets.QPushButton(self.tab_4)
        self.shutterCheckBtn.setObjectName("shutterCheckBtn")
        self.gridLayout_5.addWidget(self.shutterCheckBtn, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 2, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)
        self.responsesField = QtWidgets.QPlainTextEdit(self.tab_4)
        self.responsesField.setObjectName("responsesField")
        self.gridLayout_7.addWidget(self.responsesField, 4, 0, 1, 2)
        self.orielWidget.addTab(self.tab_4, "")
        self.gridLayout_8.addWidget(self.orielWidget, 0, 2, 6, 1)
        self.oriel_status = QtWidgets.QLabel(self.centralwidget)
        self.oriel_status.setMinimumSize(QtCore.QSize(64, 64))
        self.oriel_status.setMaximumSize(QtCore.QSize(64, 64))
        self.oriel_status.setText("")
        self.oriel_status.setObjectName("oriel_status")
        self.gridLayout_8.addWidget(self.oriel_status, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.statuslabel = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel.setMinimumSize(QtCore.QSize(64, 32))
        self.statuslabel.setMaximumSize(QtCore.QSize(64, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.statuslabel.setFont(font)
        self.statuslabel.setObjectName("statuslabel")
        self.gridLayout.addWidget(self.statuslabel, 0, 0, 1, 1)
        self.statusPictureView = QtWidgets.QLabel(self.centralwidget)
        self.statusPictureView.setMinimumSize(QtCore.QSize(64, 64))
        self.statusPictureView.setMaximumSize(QtCore.QSize(64, 64))
        self.statusPictureView.setText("")
        self.statusPictureView.setObjectName("statusPictureView")
        self.gridLayout.addWidget(self.statusPictureView, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem, 4, 0, 1, 1)
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setMinimumSize(QtCore.QSize(64, 64))
        self.connectBtn.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.connectBtn.setFont(font)
        self.connectBtn.setText("")
        self.connectBtn.setIcon(icon1)
        self.connectBtn.setIconSize(QtCore.QSize(48, 48))
        self.connectBtn.setObjectName("connectBtn")
        self.gridLayout_8.addWidget(self.connectBtn, 0, 0, 1, 1)
        self.settingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingsBtn.setMinimumSize(QtCore.QSize(64, 64))
        self.settingsBtn.setMaximumSize(QtCore.QSize(64, 64))
        self.settingsBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon3)
        self.settingsBtn.setIconSize(QtCore.QSize(60, 60))
        self.settingsBtn.setObjectName("settingsBtn")
        self.gridLayout_8.addWidget(self.settingsBtn, 5, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.fromBox = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fromBox.setFont(font)
        self.fromBox.setMinimum(180)
        self.fromBox.setMaximum(1200)
        self.fromBox.setObjectName("fromBox")
        self.gridLayout_2.addWidget(self.fromBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.toBox = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.toBox.setFont(font)
        self.toBox.setMinimum(180)
        self.toBox.setMaximum(1200)
        self.toBox.setProperty("value", 1100)
        self.toBox.setObjectName("toBox")
        self.gridLayout_2.addWidget(self.toBox, 0, 3, 1, 1)
        self.runBtn = QtWidgets.QPushButton(self.groupBox)
        self.runBtn.setMinimumSize(QtCore.QSize(64, 64))
        self.runBtn.setMaximumSize(QtCore.QSize(64, 64))
        self.runBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runBtn.setIcon(icon4)
        self.runBtn.setIconSize(QtCore.QSize(64, 64))
        self.runBtn.setObjectName("runBtn")
        self.gridLayout_2.addWidget(self.runBtn, 0, 4, 2, 1)
        self.currentWaveLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currentWaveLabel.setFont(font)
        self.currentWaveLabel.setObjectName("currentWaveLabel")
        self.gridLayout_2.addWidget(self.currentWaveLabel, 1, 0, 1, 4)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.plotWidget = PlotWidget(self.tab)
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout_4.addWidget(self.plotWidget, 1, 0, 3, 1)
        self.saveBnt = QtWidgets.QPushButton(self.tab)
        self.saveBnt.setMinimumSize(QtCore.QSize(64, 64))
        self.saveBnt.setMaximumSize(QtCore.QSize(64, 64))
        self.saveBnt.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBnt.setIcon(icon5)
        self.saveBnt.setIconSize(QtCore.QSize(60, 60))
        self.saveBnt.setFlat(False)
        self.saveBnt.setObjectName("saveBnt")
        self.gridLayout_4.addWidget(self.saveBnt, 1, 1, 1, 1)
        self.clearBtn = QtWidgets.QPushButton(self.tab)
        self.clearBtn.setMinimumSize(QtCore.QSize(64, 64))
        self.clearBtn.setMaximumSize(QtCore.QSize(64, 64))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")
        self.gridLayout_4.addWidget(self.clearBtn, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 260, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.infoFieldEdit = QtWidgets.QTextEdit(self.tab_2)
        self.infoFieldEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.infoFieldEdit.setObjectName("infoFieldEdit")
        self.gridLayout_3.addWidget(self.infoFieldEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tcpRadio = QtWidgets.QRadioButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tcpRadio.setFont(font)
        self.tcpRadio.setObjectName("tcpRadio")
        self.gridLayout_9.addWidget(self.tcpRadio, 0, 0, 1, 1)
        self.ipComboBox = QtWidgets.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ipComboBox.setFont(font)
        self.ipComboBox.setEditable(True)
        self.ipComboBox.setObjectName("ipComboBox")
        self.gridLayout_9.addWidget(self.ipComboBox, 0, 1, 1, 1)
        self.usbRadio = QtWidgets.QRadioButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.usbRadio.setFont(font)
        self.usbRadio.setObjectName("usbRadio")
        self.gridLayout_9.addWidget(self.usbRadio, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_9.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_9.addWidget(self.comboBox_2, 2, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_9, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 180))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_11.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.rel1 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel1.setObjectName("rel1")
        self.gridLayout_10.addWidget(self.rel1, 0, 0, 1, 1)
        self.rel2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel2.setObjectName("rel2")
        self.gridLayout_10.addWidget(self.rel2, 0, 1, 1, 1)
        self.rel3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel3.setObjectName("rel3")
        self.gridLayout_10.addWidget(self.rel3, 0, 2, 1, 1)
        self.rel4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel4.setObjectName("rel4")
        self.gridLayout_10.addWidget(self.rel4, 0, 3, 1, 1)
        self.rel5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel5.setObjectName("rel5")
        self.gridLayout_10.addWidget(self.rel5, 0, 4, 1, 1)
        self.rel6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.rel6.setObjectName("rel6")
        self.gridLayout_10.addWidget(self.rel6, 0, 5, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 2, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_11.addWidget(self.checkBox, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(264, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem2, 2, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_11.addWidget(self.radioButton, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_11.addWidget(self.comboBox_3, 0, 2, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 240, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_8.addWidget(self.tabWidget, 0, 1, 6, 1)
        self.device_status = QtWidgets.QLabel(self.centralwidget)
        self.device_status.setMinimumSize(QtCore.QSize(64, 64))
        self.device_status.setMaximumSize(QtCore.QSize(64, 64))
        self.device_status.setText("")
        self.device_status.setObjectName("device_status")
        self.gridLayout_8.addWidget(self.device_status, 3, 0, 1, 1)
        eqeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(eqeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1006, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        eqeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(eqeWindow)
        self.statusbar.setObjectName("statusbar")
        eqeWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(eqeWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/GUI/Icons/system-shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon6)
        self.actionQuit.setObjectName("actionQuit")
        self.actionConnect = QtWidgets.QAction(eqeWindow)
        self.actionConnect.setIcon(icon1)
        self.actionConnect.setObjectName("actionConnect")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionConnect)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(eqeWindow)
        self.orielWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(eqeWindow)

    def retranslateUi(self, eqeWindow):
        _translate = QtCore.QCoreApplication.translate
        eqeWindow.setWindowTitle(_translate("eqeWindow", "EQE"))
        self.connectBtnOriel.setText(_translate("eqeWindow", "Connect"))
        self.statusLabel.setText(_translate("eqeWindow", "Not connected"))
        self.waveBtn.setText(_translate("eqeWindow", "Wave?"))
        self.nmRadioBtn.setText(_translate("eqeWindow", "nm"))
        self.evRadioBtn.setText(_translate("eqeWindow", "eV"))
        self.goBtn.setText(_translate("eqeWindow", "Go"))
        self.waveLabel.setText(_translate("eqeWindow", "Current wave [nm]: (not set)"))
        self.shutterStatusLabel.setText(_translate("eqeWindow", "?"))
        self.shutterToggleBtn.setText(_translate("eqeWindow", "Open/Close"))
        self.shutterCheckBtn.setText(_translate("eqeWindow", "Check?"))
        self.label_3.setText(_translate("eqeWindow", "Shutter:"))
        self.label_4.setText(_translate("eqeWindow", "Responses"))
        self.orielWidget.setTabText(self.orielWidget.indexOf(self.tab_4), _translate("eqeWindow", "ORIEL"))
        self.statuslabel.setText(_translate("eqeWindow", "Status"))
        self.connectBtn.setToolTip(_translate("eqeWindow", "Connect"))
        self.settingsBtn.setToolTip(_translate("eqeWindow", "Settings"))
        self.groupBox.setTitle(_translate("eqeWindow", "Measurement:"))
        self.label.setText(_translate("eqeWindow", "From [λ, nm]:"))
        self.label_2.setText(_translate("eqeWindow", "To [λ, nm]:"))
        self.currentWaveLabel.setText(_translate("eqeWindow", "Current position [nm] - {lambda}."))
        self.saveBnt.setToolTip(_translate("eqeWindow", "Save"))
        self.clearBtn.setToolTip(_translate("eqeWindow", "Clear"))
        self.clearBtn.setText(_translate("eqeWindow", "CLR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("eqeWindow", "M"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("eqeWindow", "ERR"))
        self.tcpRadio.setText(_translate("eqeWindow", "TCP/IP"))
        self.usbRadio.setText(_translate("eqeWindow", "USB"))
        self.label_5.setText(_translate("eqeWindow", "Device:"))
        self.groupBox_2.setTitle(_translate("eqeWindow", "PINS && RELAYS"))
        self.radioButton_2.setText(_translate("eqeWindow", "Use Relays"))
        self.rel1.setText(_translate("eqeWindow", "1"))
        self.rel2.setText(_translate("eqeWindow", "2"))
        self.rel3.setText(_translate("eqeWindow", "3"))
        self.rel4.setText(_translate("eqeWindow", "4"))
        self.rel5.setText(_translate("eqeWindow", "5"))
        self.rel6.setText(_translate("eqeWindow", "6"))
        self.checkBox.setText(_translate("eqeWindow", "Use Relay"))
        self.radioButton.setText(_translate("eqeWindow", "One Contact"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("eqeWindow", "SETTINGS"))
        self.menuFile.setTitle(_translate("eqeWindow", "File"))
        self.actionQuit.setText(_translate("eqeWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("eqeWindow", "Ctrl+Q"))
        self.actionConnect.setText(_translate("eqeWindow", "Connect"))
from pyqtgraph import PlotWidget
import eqerc_rc
