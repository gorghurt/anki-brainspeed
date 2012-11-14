#!/usr/bin/python
# -*- coding: utf-8 -*-




import sys
from PyQt4 import QtGui
import random
import time
import threading
import thread
#import sys #für lambda prints
from numpy import * #für arange


Anzahl_Antworten= 2
questions=["a?","b?","c?","d?","e?","f","g","h","i","j"]
answers=["a?","b?","c?","d?","e?","f","g","h","i","j"]
zeit=3
rightfaktor=0.9
wrongfaktor=1.1

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
    
        self.resize(640,480)
        self.setWindowTitle('Anki-BrainSpeed')    
        self.show()
        
        #Variablen instanzen(timer) etc
        self.time=zeit
        self.timer=timer(self.time,lambda: self.refreshtimelabel(),lambda: self.wrong())
        
        #erster Refresh  (später entfernen und durch start dialog ersetzen, oder dieses fesnter nach start dialog erstellen)
 
        self.refresh(True)
        
        
    def refreshtimelabel(self):
	self.timelabel.setText(str(self.timer.counter));
	
    def right(self):
      print("right")
      self.time=self.time*rightfaktor
      self.refresh()
      
      
    def wrong(self):
      print("wrong")
      self.time=self.time*wrongfaktor
      self.refresh()
      
      
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
	if first != True:
	  self.timelabel.setText(str(self.time))
	  self.timer.runTime=self.time
	  thread.start_new_thread (self.timer.run())
 #timer verhindert gui. qtimer aus qt angucken    
class timer(threading.Thread):
#based on some code i found while using google. forgot from where it is. if you are the creator, contact me please.
#I would be glad to mention you.
    def __init__(self, seconds, refresh , do):
      self.runTime = seconds
      self.counter=self.runTime 
      self.action=do
      self.refresh=refresh
      threading.Thread.__init__(self)
    def run(self):
      self.counter=self.runTime 
      for sec in arange(0,self.runTime,0.1):#range(0,self.runTime*10,0.1):
	print self.counter
	time.sleep(0.1)
	self.counter-=0.1
	self.refresh()
      self.action()
      print "Done."
def main():
    
    app = QtGui.QApplication(sys.argv)
    w = Window()
    #timex =timer(100, lambda: sys.stdout.write('foo\n'))
    #timex.runTime=3
    #timex.run()
    #sys.exit(app.exec_())
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
