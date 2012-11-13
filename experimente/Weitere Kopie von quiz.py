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

Anzahl_Antworten= 4

class Window(QtGui.QWidget):
    btnlist = []
    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
	n=Anzahl_Antworten
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
	okButton.clicked.connect(lambda: self.right())
	cancelButton.clicked.connect(lambda: self.wrong())
        hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        #grid.addWidget(okButton,2,0)
        #grid.addWidget(cancelButton,2,1)
	
        vbox = QtGui.QVBoxLayout()
        #vbox.setStretch(2,1)
        grid.addWidget(timelabel,0,n-1)
        grid.addWidget(lebenlabel,0,0)
        grid.addWidget(label,1,0,1,n-1)
        #vbox.setStretch(2,1)
        grid.setRowStretch(1,3)
        grid.setRowStretch(2,2)
        vbox.addLayout(hbox)
        #hbox.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
        #Dynamisches Button erzeugen
        self.btnlist=[]
        
        for i in range(0,n) :
	  #Button=QtGui.QPushButton("bla")
	  #Button.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	  #grid.addWidget(Button,2,i)
	 # command=lambda x=i: self.right(x)
	  #Button.clicked.connect(command)
	  #Button.clicked.connect(lambda: self.check())
	  #print i
	  #x= int(i)
	  self.btnlist.append(QtGui.QPushButton("bla"))
	  
	  #self.btnlist[i].clicked.connect(lambda: self.right(i))#  klappt nicht, alle geben das gleiche aus daher anders
	  self.btnlist[i].clicked.connect(lambda value=i : self.check(value))
	  self.btnlist[i].setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	  grid.addWidget(self.btnlist[i],2,i)
	  
        self.setLayout(grid)    
        
        self.resize(640,480)
        self.setWindowTitle('Buttons')    
        self.show()
        
    def check(self,i):
      print i
      
	
    def right(self,n):
      print(n)
    def wrong(self):
      print("wrong")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
