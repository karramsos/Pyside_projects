#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Display image on the window

Author : Sukhvinder Singh | karramsos@gmail.com | @karramsos
"""

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("pb_anon.jpg")
        
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Anon')
        self.show()
    
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

    
    
