# -*- coding: utf-8 -*-


#
# Created by: PyQt5 UI code generator 5.13.0
#



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from SNMP import SNMP_MIB_WALK
from SNMP import SNMP_MIB_GET
from SNMP import SNMP_OID_GET



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/JonathanMelcher/AppData/Local/Temp/QTSNMP_MAINVdOjii.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(690, 529)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 480, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.HOST = QtWidgets.QLineEdit(Dialog)
        self.HOST.setGeometry(QtCore.QRect(140, 50, 113, 22))
        self.HOST.setObjectName("HOST")
        self.COMMUNITY = QtWidgets.QLineEdit(Dialog)
        self.COMMUNITY.setGeometry(QtCore.QRect(160, 90, 113, 22))
        self.COMMUNITY.setObjectName("COMMUNITY")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 121, 16))
        self.label_2.setObjectName("label_2")
        self.OID_BUTTON = QtWidgets.QPushButton(Dialog)
        self.OID_BUTTON.setGeometry(QtCore.QRect(170, 160, 75, 24))
        self.OID_BUTTON.setObjectName("OID_BUTTON")
        self.OID_BUTTON.clicked.connect(self.SET_TEXT_OID)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 121, 16))
        self.label_3.setObjectName("label_3")
        self.OID = QtWidgets.QLineEdit(Dialog)
        self.OID.setGeometry(QtCore.QRect(140, 120, 113, 22))
        self.OID.setObjectName("OID")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 210, 121, 16))
        self.label_4.setObjectName("label_4")
        self.MIB = QtWidgets.QLineEdit(Dialog)
        self.MIB.setGeometry(QtCore.QRect(130, 210, 113, 22))
        self.MIB.setText("")
        self.MIB.setObjectName("MIB")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 280, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 121, 16))
        self.label_5.setObjectName("label_5")
        self.VAR = QtWidgets.QLineEdit(Dialog)
        self.VAR.setGeometry(QtCore.QRect(130, 240, 113, 22))
        self.VAR.setText("")
        self.VAR.setObjectName("VAR")
        self.INSTANCE = QtWidgets.QLineEdit(Dialog)
        self.INSTANCE.setGeometry(QtCore.QRect(130, 320, 113, 22))
        self.INSTANCE.setText("")
        self.INSTANCE.setObjectName("INSTANCE")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 320, 121, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 350, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.SNMP_LIST = QtWidgets.QListWidget(Dialog)
        self.SNMP_LIST.setGeometry(QtCore.QRect(360, 90, 256, 192))
        self.SNMP_LIST.setObjectName("SNMP_LIST")
        item = QtWidgets.QListWidgetItem()
        self.SNMP_LIST.addItem(item)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Host"))
        self.label_2.setText(_translate("Dialog", "Community"))
        self.OID_BUTTON.setText(_translate("Dialog", "OID GET"))


        self.label_3.setText(_translate("Dialog", "OID"))
        self.label_4.setText(_translate("Dialog", "MIB"))
        self.pushButton_2.setText(_translate("Dialog", "Walk"))
        self.label_5.setText(_translate("Dialog", "Variable"))
        self.label_6.setText(_translate("Dialog", "Instance"))
        self.pushButton_3.setText(_translate("Dialog", "Get"))
        __sortingEnabled = self.SNMP_LIST.isSortingEnabled()
        self.SNMP_LIST.setSortingEnabled(False)
        item = self.SNMP_LIST.item(0)
        item.setText(_translate("Dialog", " ",))
        self.SNMP_LIST.setSortingEnabled(__sortingEnabled)

    def SET_TEXT_OID(self):
        print ("OID")

        __sortingEnabled = self.SNMP_LIST.isSortingEnabled()
        self.SNMP_LIST.setSortingEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        item = self.SNMP_LIST.item(0)
        item.setText(_translate("Dialog", " "))
        self.SNMP_LIST.setSortingEnabled(__sortingEnabled)
        item = self.SNMP_LIST.item(0)
        item.setText(_translate("Dialog", SNMP_OID_GET(self.HOST,self.COMMUNITY,self.OID)))
        self.SNMP_LIST.setSortingEnabled(__sortingEnabled)



app=QApplication(sys.argv)
window=QDialog()
ui=Ui_Dialog()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
