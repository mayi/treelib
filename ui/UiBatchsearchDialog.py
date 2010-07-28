# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batchsearch.ui'
#
# Created: Sat Jun 26 17:28:41 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_BatchsearchDialog(object):
    def setupUi(self, BatchsearchDialog):
        BatchsearchDialog.setObjectName("BatchsearchDialog")
        BatchsearchDialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(BatchsearchDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.nameTextEdit = QtGui.QPlainTextEdit(BatchsearchDialog)
        self.nameTextEdit.setGeometry(QtCore.QRect(10, 10, 381, 251))
        self.nameTextEdit.setObjectName("nameTextEdit")

        self.retranslateUi(BatchsearchDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), BatchsearchDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), BatchsearchDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BatchsearchDialog)

    def retranslateUi(self, BatchsearchDialog):
        BatchsearchDialog.setWindowTitle(QtGui.QApplication.translate("BatchsearchDialog", "批量搜索", None, QtGui.QApplication.UnicodeUTF8))

