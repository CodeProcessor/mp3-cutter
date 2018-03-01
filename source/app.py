# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mp3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(510, 151)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 20, 97, 26))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 251, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 211, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 41, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 60, 97, 26))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 40, 81, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 41, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 40, 81, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 50, 41, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Mp3 Cutter - v_0.1", None))
        self.pushButton.setText(_translate("MainWindow", "Select File", None))
        self.label.setText(_translate("MainWindow", "Filename:", None))
        self.label_2.setText(_translate("MainWindow", "--please-select--", None))
        self.label_3.setText(_translate("MainWindow", "Output name:", None))
        self.label_4.setText(_translate("MainWindow", ".mp3", None))
        self.pushButton_2.setText(_translate("MainWindow", "Convert", None))
        self.label_5.setText(_translate("MainWindow", "Start:", None))
        self.label_6.setText(_translate("MainWindow", "End :", None))
        
        self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.convertFile)

    def selectFile(self):
        self.file_name = str(QFileDialog.getOpenFileName())
        self.label_2.setText(self.file_name)
        b_name = os.path.basename(str(self.file_name))
        self.lineEdit.setText(str(b_name))
        
    def convertFile(self):
        print "convert"
        o_name = str(self.lineEdit.text())
#         print o_name
        if o_name == "":
            o_name = os.path.basename(self.file_name)
        
        start_time = self.lineEdit_2.text()
        end_time = self.lineEdit_3.text()
#         print start_time, end_time
        duration = np.int(str(end_time)) - np.int(str(start_time))
        o_path = os.path.join(os.path.dirname(self.file_name), o_name)

        start_time_format = '00:'+start_time+':00'
        command = 'ffmpeg' +' -ss ' + start_time_format + ' -i ' + self.file_name + ' -t ' + str(duration) + ' -acodec copy ' + o_path
        print command
        os.system(str(command))
#         if o_name.split('.')[1] is None:
#             print "None"

import os
import numpy as np

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

