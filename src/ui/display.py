# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/display.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self._display = QtWidgets.QTableView(self.centralwidget)
        self._display.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._display.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self._display.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self._display.setTextElideMode(QtCore.Qt.ElideNone)
        self._display.setWordWrap(False)
        self._display.setObjectName("_display")
        self._display.horizontalHeader().setVisible(False)
        self._display.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self._display, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._text = QtWidgets.QLineEdit(self.centralwidget)
        self._text.setObjectName("_text")
        self.horizontalLayout_2.addWidget(self._text)
        self._run = QtWidgets.QPushButton(self.centralwidget)
        self._run.setObjectName("_run")
        self.horizontalLayout_2.addWidget(self._run)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged['int'].connect(self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._run.setText(_translate("MainWindow", "Панеслася!"))
        self.label.setText(_translate("MainWindow", "Скорость"))
        self.label_2.setText(_translate("MainWindow", "0"))

