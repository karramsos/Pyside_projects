#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Drag and drop text with QtGui.QlineEdit and drop it on the QtGui.QPushButton
To use it write text in the text field, select the text and drag it to the
button and the button will get the same text as the textfield.

Author : Sukhvinder Singh | karramsos@gmail.com | @karramsos
"""

import sys
from PySide import QtGui, QtCore

class Button(QtGui.QPushButton):
    
    def __init__(self, title, parent):
        
        super(Button, self).__init__(title, parent)
        
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, e):
        
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        self.setText(e.mimeData().text())
        

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        qe = QtGui.QLineEdit('',self)
        qe.setDragEnabled(True)
        qe.move(30, 65)
        
        button = Button("Button", self)
        button.move(190, 65)
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Simple Drag & Drop')
        self.show()
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

    
    
