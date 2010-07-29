# -*- coding: utf-8 -*-

import sys
from ui.UiMainWindow import Ui_MainWindow
from ui.UiBatchsearchDialog import Ui_BatchsearchDialog
from PyQt4 import QtGui, QtCore
import dataservice

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):

        self.dataService = dataservice.DataService()
        
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setTableContextMenu()

        #点击action_search_byname弹出中文树种名搜索
        self.connect(self.action_search_byname, QtCore.SIGNAL('triggered()'), self.showSearchNameDialog)
        #点击action_search_bylatin弹出拉丁名搜索
        self.connect(self.action_search_bylatin, QtCore.SIGNAL('triggered()'), self.showSearchLatinDialog)
        #点击action_search_byname_batch弹出中文树种名批量搜索
        self.connect(self.action_search_byname_batch, QtCore.SIGNAL('triggered()'), self.showNameBatchsearchDialog)
        #点击action_search_bylatin_batch弹出中文树种名批量搜索
        self.connect(self.action_search_bylatin_batch, QtCore.SIGNAL('triggered()'), self.showLatinBatchsearchDialog)
        
        #复制
        self.connect(self.action_edit_copy, QtCore.SIGNAL('triggered()'), self.copyCells)

        self.toolBar.addAction(self.action_search_byname)
        self.toolBar.addAction(self.action_search_bylatin)
        self.toolBar.addAction(self.action_search_byname_batch)
        self.toolBar.addAction(self.action_search_bylatin_batch)
        self.toolBar.addAction(self.action_edit_edit)
        #self.toolBar.addAction(self.action_edit_copy)

    #关闭事件
    def closeEvent(self, event):
        event.accept()
    
    #中文树种名搜索条件输入框
    def showSearchNameDialog(self):
        name, ok = QtGui.QInputDialog.getText(self, u"按中文名搜索", u"中文名:", QtGui.QLineEdit.Normal)
        if ok and not name.isEmpty():
            self.searchByName(unicode(name.toUtf8(), 'utf-8'))

    #中文树种名搜索
    def searchByName(self, name):
        data = self.dataService.queryDataByName(name)
        self.putDataIntoTable(data)

    #拉丁名搜索条件输入框
    def showSearchLatinDialog(self):
        latin, ok = QtGui.QInputDialog.getText(self, u"按拉丁名搜索", u"拉丁名:", QtGui.QLineEdit.Normal)
        if ok and not latin.isEmpty():
            self.searchByLatin(unicode(latin.toUtf8(), 'utf-8'))

    #拉丁名搜索
    def searchByLatin(self, latin):
        data = self.dataService.queryDataByLatin(latin)
        self.putDataIntoTable(data)

    #中文树种名批量搜索条件对话框
    def showNameBatchsearchDialog(self):
        batchsearchDialog = BatchsearchDialog('中文树种名批量搜索')
        batchsearchDialog.show()
        if batchsearchDialog.exec_():
            text = batchsearchDialog.getText()
            names = unicode(text.toUtf8(), 'utf-8').split('\n')
            self.searchByNames(names)
    
    #中文树种名批量搜索条件对话框
    def showLatinBatchsearchDialog(self):
        batchsearchDialog = BatchsearchDialog('拉丁树种名批量搜索')
        batchsearchDialog.show()
        if batchsearchDialog.exec_():
            text = batchsearchDialog.getText()
            latins = unicode(text.toUtf8(), 'utf-8').split('\n')
            self.searchByLatins(latins)

    #中文树种名批量搜索
    def searchByNames(self, names):
        data = self.dataService.queryDataByNamesExactly(names)
        self.putDataIntoTable(data)
    
    #拉丁名批量搜索
    def searchByLatins(self, latins):
        data = self.dataService.queryDataByLatinsExactly(latins)
        self.putDataIntoTable(data)
    
    #将数据放入表格
    def putDataIntoTable(self, data):
        self.table.clearContents()
        count = len(data)
        self.statusbar.showMessage(QtCore.QString(unicode('搜索结果：' + str(count) + '条记录', 'utf-8')))
        self.table.setRowCount(count)
        row = 0
        for d in data:
            self.table.setItem(row, 0, QtGui.QTableWidgetItem(d['name']))
            self.table.setItem(row, 1, QtGui.QTableWidgetItem(d['latin']))
            self.table.setItem(row, 2, QtGui.QTableWidgetItem(d['cate']))
            self.table.setItem(row, 3, QtGui.QTableWidgetItem(d['shxx']))
            self.table.setItem(row, 4, QtGui.QTableWidgetItem(d['size_qm']))
            self.table.setItem(row, 5, QtGui.QTableWidgetItem(d['size_gf']))
            self.table.setItem(row, 6, QtGui.QTableWidgetItem(d['size_gm']))
            self.table.setItem(row, 7, QtGui.QTableWidgetItem(d['size_cm']))
            self.table.setItem(row, 8, QtGui.QTableWidgetItem(d['size_tb']))
            self.table.setItem(row, 9, QtGui.QTableWidgetItem(d['szsd']))
            self.table.setItem(row, 10, QtGui.QTableWidgetItem(d['sx']))
            self.table.setItem(row, 11, QtGui.QTableWidgetItem(d['gstz']))
            self.table.setItem(row, 12, QtGui.QTableWidgetItem(d['hs']))
            self.table.setItem(row, 13, QtGui.QTableWidgetItem(d['khlx']))
            self.table.setItem(row, 14, QtGui.QTableWidgetItem(d['hq']))
            self.table.setItem(row, 15, QtGui.QTableWidgetItem(d['fxbw']))
            self.table.setItem(row, 16, QtGui.QTableWidgetItem(d['gq']))
            self.table.setItem(row, 17, QtGui.QTableWidgetItem(d['gs']))
            self.table.setItem(row, 18, QtGui.QTableWidgetItem(d['ys']))
            self.table.setItem(row, 19, QtGui.QTableWidgetItem(d['zgys']))
            self.table.setItem(row, 20, QtGui.QTableWidgetItem(d['zttz']))
            self.table.setItem(row, 21, QtGui.QTableWidgetItem(d['gyz']))
            self.table.setItem(row, 22, QtGui.QTableWidgetItem(d['nhx']))
            self.table.setItem(row, 23, QtGui.QTableWidgetItem(d['sfyz']))
            self.table.setItem(row, 24, QtGui.QTableWidgetItem(d['tryz']))
            self.table.setItem(row, 25, QtGui.QTableWidgetItem(d['kx']))
            self.table.setItem(row, 26, QtGui.QTableWidgetItem(d['ylyt']))
            self.table.setItem(row, 27, QtGui.QTableWidgetItem(d['jjyt']))
            self.table.setItem(row, 28, QtGui.QTableWidgetItem(d['bz']))
            self.table.setItem(row, 29, QtGui.QTableWidgetItem(d['zrfbq']))
            row = row + 1
        self.table.resizeColumnsToContents()

    #表格内容复制
    def copyCells(self):
        selRange  = self.table.selectedRanges()[0] #just take the first range
        topRow = selRange.topRow()
        bottomRow = selRange.bottomRow()
        rightColumn = selRange.rightColumn()
        leftColumn = selRange.leftColumn()
        clipStr = QtCore.QString()
        for row in xrange(topRow, bottomRow + 1):
            for col in xrange(leftColumn, rightColumn + 1):
                cell = self.table.item(row, col)
                if cell:
                    clipStr.append(cell.text())
                else:
                    clipStr.append(QtCore.QString(""))
                clipStr.append(QtCore.QString("\t"))
            clipStr.chop(1)
            clipStr.append(QtCore.QString("\r\n"))
        cb = QtGui.QApplication.clipboard()
        cb.setText(clipStr)
    
    def setTableContextMenu(self):
        self.contextmenu_copy = QtGui.QAction("&Copy", self.table)
        self.connect(self.contextmenu_copy, QtCore.SIGNAL('triggered()'), self.copyCells)
        self.table.addAction(self.contextmenu_copy)

class BatchsearchDialog(QtGui.QDialog, Ui_BatchsearchDialog):
    def __init__(self, title):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("BatchsearchDialog", title, None, QtGui.QApplication.UnicodeUTF8))

    def getText(self):
        return self.nameTextEdit.toPlainText()
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
