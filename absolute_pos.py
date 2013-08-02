#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This program shows three labels on a window using absolute positioning.

Author : Sukhvinder Singh | karramsos@gmail.com | @karramsos
"""

import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        label1 = QtGui.QLabel('Zetcode', self)
        label1.move(15, 10)
        
        label2 = QtGui.QLabel('tutorials', self)
        label2.move(35, 40)
        
        label3 = QtGui.QLabel('for programmers', self)
        label3.move(55, 70)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
               
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()#!/usr/bin/env python

