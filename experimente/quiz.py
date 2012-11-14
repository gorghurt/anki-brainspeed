#!/usr/bin/python
# -*- coding: utf-8 -*-




import sys
from PyQt4 import QtGui
import random

Anzahl_Antworten= 2
questions=["a?","b?","c?","d?","e?","f","g","h","i","j"]
answers=["a?","b?","c?","d?","e?","f","g","h","i","j"]

class Window(QtGui.QWidget):    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
	n=Anzahl_Antworten
	
	#grid Layout:
        grid=QtGui.QGridLayout()
        
        #Label 
        self.label=QtGui.QLabel("Frage")
        self.timelabel=QtGui.QLabel("time")
        self.lebenlabel=QtGui.QLabel("Leben")
        
        self.label.setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

	#Label ins Grid einfügen
        grid.addWidget(self.timelabel,0,n-1)
        grid.addWidget(self.lebenlabel,0,0)
        grid.addWidget(self.label,1,0,1,n-1)

        #Stretch werte Setzen (Fragen label und Butttons sollen größer sein als Rest)
        grid.setRowStretch(1,3)
        grid.setRowStretch(2,2)


        #Dynamisches Button erzeugen
        self.btnlist=[]
        
        for i in range(0,n) :

	  self.btnlist.append(QtGui.QPushButton(str(i)))
	  
	  self.btnlist[i].setSizePolicy(QtGui.QSizePolicy( QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	  grid.addWidget(self.btnlist[i],2,i)
	
	#Fenster erstellen
        self.setLayout(grid)    
        #erster Refresh  (später entfernen und durch start dialog ersetzen, oder dieses fesnter nach start dialog erstellen)
        self.refresh(True)
        
        self.resize(640,480)
        self.setWindowTitle('Anki-BrainSpeed')    
        self.show()
        
    def check(self,i):
      print i
      
	
    def right(self):
      print("right")
      self.refresh()
      
      
    def wrong(self):
      print("wrong")
      
      
    def refresh(self, first=False):
      right = random.randint(0, len(answers)-1 )
      self.label.setText(questions[right])
      r=random.randint(0, Anzahl_Antworten-1)
      print("refresh"+ str(r))
      for i in range(0, Anzahl_Antworten):
	if i == r:
	  if first != True:
	    self.btnlist[i].clicked.disconnect()
	  self.btnlist[i].clicked.connect(lambda: self.right())
	  self.btnlist[i].setText(answers[right])
	else:
	  if first != True:
	    self.btnlist[i].clicked.disconnect()
	  self.btnlist[i].clicked.connect(lambda: self.wrong())
	  wrong=random.randint(0,len(answers)-1)
	  if wrong==right:
	      if wrong+1 < len(answers):
		wrong=wrong+1
	      else:
		wrong=wrong-1
	  self.btnlist[i].setText(answers[wrong])

def main():
    
    app = QtGui.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
