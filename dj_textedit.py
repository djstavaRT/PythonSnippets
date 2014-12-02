#!/usr/bin/env python

import sys
import os
from PyQt4.QtGui import *

class TextEdit(QMainWindow):

    def __init__(self):
        super(TextEdit, self).__init__()
        #font = QFont("Courier", 11)
        #self.setFont(font)
        self.filename = False
        self.Ui()

    def Ui(self):
        newFile = QAction('New', self)
        openFile = QAction('Open', self)
        saveFile = QAction('Save', self)
        quitApp = QAction('Quit', self)

        copyText = QAction('Copy', self)
        pasteText = QAction('Paste', self)

        newFile.setShortcut('Ctrl+N')
        newFile.triggered.connect(self.newFile)
        openFile.setShortcut('Ctrl+O')
        openFile.triggered.connect(self.openFile)
        saveFile.setShortcut('Ctrl+S')
        saveFile.triggered.connect(self.saveFile)
        quitApp.setShortcut('Ctrl+Q')
        quitApp.triggered.connect(self.close)
        copyText.setShortcut('Ctrl+C')
        copyText.triggered.connect(self.copyFunc)
        pasteText.setShortcut('Ctrl+V')
        pasteText.triggered.connect(self.pasteFunc)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)

        menuFile = menubar.addMenu('&File')
        menuFile.addAction(newFile)
        menuFile.addAction(openFile)
        menuFile.addAction(saveFile)
        menuFile.addAction(quitApp)

        menuEdit = menubar.addMenu('&Edit')
        menuEdit.addAction(copyText)
        menuEdit.addAction(pasteText)

        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setMenuWidget(menubar)
        self.setMenuBar(menubar)
        self.setGeometry(200,200,480,320)
        self.setWindowTitle('TextEdit')
        self.show()

    def copyFunc(self):
        self.text.copy()

    def pasteFunc(self):
        self.text.paste()

    def unSaved(self):
        destroy = self.text.document().isModified()

        if destroy == False:
            return False
        else:
            detour = QMessageBox.question(self,
                "Hold your horses.",
                "File has unsaved changes. Save now?",
                QMessageBox.Yes|QMessageBox.No|
                QMessageBox.Cancel)
            if detour == QMessageBox.Cancel:
                return True
            elif detour == QMessageBox.No:
                return False
            elif detour == QMessageBox.Yes:
                return self.saveFile()

        return True

    def saveFile(self):
        if self.filename is False:
            self.filename = QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser('~'))
        else:
            f = open(self.filename, 'w')
            filedata = self.text.toPlainText()
            f.write(filedata)
            f.close()

    def newFile(self):
        if not self.unSaved():
            self.text.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', os.path.expanduser("~"))
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)
        f.close()

    def closeEvent(self, event):
        if self.unSaved():
            event.ignore()
        else:
            exit

def main():
    app = QApplication(sys.argv)
    editor = TextEdit()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
