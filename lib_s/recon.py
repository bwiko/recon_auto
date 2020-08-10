# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recon.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recon(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(321, 452)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setObjectName("treeWidget")
        
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Close = QtWidgets.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/notwork.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close.setIcon(icon1)
        self.Close.setIconSize(QtCore.QSize(40, 40))
        self.Close.setAutoRaise(True)
        self.Close.setObjectName("Close")
        self.horizontalLayout_2.addWidget(self.Close)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.attack = QtWidgets.QToolButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/1298514.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attack.setIcon(icon2)
        self.attack.setIconSize(QtCore.QSize(40, 40))
        self.attack.setAutoRaise(True)
        self.attack.setObjectName("attack")
        self.horizontalLayout_2.addWidget(self.attack)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RECOn"))
        self.label.setText(_translate("Form", "domain "))
        self.treeWidget.headerItem().setText(0, _translate("Form", "command on the domain name "))
        
        self.Close.setText(_translate("Form", "..."))
        self.Close.setShortcut(_translate("Form", "Esc"))
        self.label_2.setText(_translate("Form", "        "))
        self.attack.setText(_translate("Form", "..."))
        self.attack.setShortcut(_translate("Form", "Return"))
import icon_rc
