#!/usr/bin/python
# -*- coding: utf-8 -*-




import sys
from PyQt4 import QtGui, QtCore
import random
import time
import threading
import thread
#import sys #für lambda prints
from numpy import * #für arange


Anzahl_Antworten= 4
questions=["a?","b?","c?","d?","e?","f","g","h","i","j"]
answers=["a?","b?","c?","d?","e?","f","g","h","i","j"]
zeit=3000
rightfaktor=0.9
times_to_rightfaktor=4
times_to_combo_bonus=10
wrongfaktor=1.1
times_to_wrongfaktor=1
wrong_breaks_combo=False #noch nicht implementiert
wrong_counts_as_combo=False #noch nicht drin

time_to_next_round=1000

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
	self.counter=zeit
        # Create a QTimer
	self.timer = QtCore.QTimer()
	self.timer.timeout.connect(lambda: self.refreshtimelabel()) #timer ruft refreshtimelabel auf und die funktion überprüft selbst ob die zeit abgelaufen ist
	self.combo=0
	self.right_time_combo=0
	self.wrong_time_combo=0
	#self.next_round_timer=QtCoreTimer()
	#self.next_round_timer.timeout.
	# Connect it to f
	# Call f() every 5 seconds
	
        
        #erster Refresh  (später entfernen und durch start dialog ersetzen, oder dieses fesnter nach start dialog erstellen)
 
        self.refresh(True)
        
        
    def refreshtimelabel(self):
      self.counter-=100
      self.timelabel.setText(str(self.counter));
      if self.counter<=0:
	self.timer.stop()
	self.wrong()
	
    def right(self):
      self.right_time_combo+=1
      print("right")
      if self.right_time_combo==times_to_rightfaktor:
	self.time=self.time*rightfaktor
	self.right_time_combo=0
	print("righttimefaktor")
      #if self.combo=times_to_combo_bonus:
	#life+=1
      self.refresh()
      
      
    def wrong(self):
      print("wrong")
      self.label.setText("WRONG -1")
      self.time=self.time*wrongfaktor
      #self.next_round_timer.start(time_to_next_round)
      QtCore.QTimer.singleShot(time_to_next_round,lambda: self.refresh())
      
      
    def refresh(self, first=False):
      #richtige antwort zufällig wählen
      right = random.randint(0, len(answers)-1 )
      #frage setzen
      self.label.setText(questions[right])
      #button für richtige antwort zufälig wählen
      r=random.randint(0, Anzahl_Antworten)# -1 entfernt weil letzter button nie right
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
	  #zufällige antwort != richtige antwort wählen und auf button schreiben 
	  wrong=random.randint(0,len(answers)-1)
	  if wrong==right:
	      if wrong+1 < len(answers):
		wrong=wrong+1
	      else:
		wrong=wrong-1
	  self.btnlist[i].setText(answers[wrong])
	if first != True:
	  
	  
	  self.counter=self.time
	  self.timelabel.setText(str(self.time))
	  
	  self.timer.start(100)
	  
	  
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
