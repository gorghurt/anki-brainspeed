#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we position two push
buttons in the bottom-right corner 
of the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        grid=QtGui.QGridLayout()
        label=QtGui.QLabel("blargh")
        timelabel=QtGui.QLabel("time")
        lebenlabel=QtGui.QLabel("Leben")
        label.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
        okButton = QtGui.QPushButton()
        cancelButton = QtGui.QPushButton("Cancel")
	okButton.setText("bla")
	okButton.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	cancelButton.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        grid.addWidget(okButton,2,0)
        grid.addWidget(cancelButton,2,1)

        vbox = QtGui.QVBoxLayout()
        #vbox.setStretch(2,1)
        grid.addWidget(timelabel,0,1)
        grid.addWidget(lebenlabel,0,0)
        grid.addWidget(label,1,0,1,1)
        #vbox.setStretch(2,1)
        grid.setRowStretch(1,3)
        grid.setRowStretch(2,2)
        vbox.addLayout(hbox)
        #hbox.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
        self.setLayout(grid)    
        
        self.resize(640,480)
        self.setWindowTitle('Buttons')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
