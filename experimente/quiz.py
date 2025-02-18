#!/usr/bin/python
# -*- coding: utf-8 -*-

#TODO:
  #segmentation fault ausmerzen
  #Timer beginnt absichtlich erst nach erster antwort: anfangs menü hinlegen(start button oder ähnliches)
  #evtl zeitveräderungsverhalten in wrong wie in right mahcen(also mit combo wrongtimecombo)
  
#annahme: segmentation fault kommt durch zu schnelles klicken wegen qt, daher buttns diablen bis fertig
#hat nichts gebracht, aber das buttons disablen bleibt drin um doppelgeklickte falsche antworten zu vermeiden

import sys
from PyQt4 import QtGui, QtCore
#from PyQt4 import *
import random
import time
import threading
import thread
#import sys #für lambda prints
from numpy import * #für arange


Anzahl_Antworten= 2 #wie viele buttons sollen angezeigt werden
questions=["a?","b?","c?","d?","e?","f","g","h","i","j"]
answers=["a?","b?","c?","d?","e?","f","g","h","i","j"]
questions=[u"わかた",u"はは"] 
answers=[u"わかた",u"はは"]
zeit=3000
rightfaktor=0.9
times_to_rightfaktor=4
times_to_combo_bonus=10
wrongfaktor=1.1
times_to_wrongfaktor=1
wrong_breaks_combo=False #noch nicht implementiert
wrong_counts_as_combo=False #noch nicht drin

Lives_at_start=3

time_to_next_round=500
time_to_next_round_w=time_to_next_round #pausen zeit bei falsch antwort
time_to_next_round_r=time_to_next_round #pausen zeit bei richtiger antwort

class Window(QtGui.QWidget):    
    def __init__(self):
        super(Window, self).__init__()
        
        self.initUI()
        
    def initUI(self):
	n=Anzahl_Antworten
	self.lives=Lives_at_start
	#grid Layout:
        grid=QtGui.QGridLayout()
        
        #Label 
        self.label=StretchedLabel("Frage")
        self.timelabel=StretchedLabel("time")
        self.lebenlabel=StretchedLabel("Leben")
        
	self.label.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	self.timelabel.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	self.lebenlabel.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
	#Label ins Grid einfügen
        grid.addWidget(self.timelabel,0,n-1)
        grid.addWidget(self.lebenlabel,0,0)
        grid.addWidget(self.label,1,0,1,n-1)

        #Stretch werte Setzen (Fragen label und Butttons sollen größer sein als Rest)
        grid.setRowStretch(0,1)
        grid.setRowStretch(1,6)
        grid.setRowStretch(2,4)


        #Dynamisches Button erzeugen
        self.btnlist=[]
        
        for i in range(0,n) :

	  self.btnlist.append(StretchedButton())
	  self.btnlist[i].setText(str(i))
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
      #timer stoppen
      self.timer.stop()
      #buttons deaktivieren
      for i in range(0,Anzahl_Antworten):
	self.btnlist[i].setEnabled(False)
      
      print("right")
      self.label.setText("right")
      
      #zeitverlust (spiel wird schneller) wenn genügend oft richtig
      self.right_time_combo+=1
      if self.right_time_combo==times_to_rightfaktor:
	self.time=self.time*rightfaktor
	self.right_time_combo=0
	print("righttimefaktor")
      #Später: Lebensbonus
      #if self.combo=times_to_combo_bonus:   
	#life+=1
      #self.refresh()  
      
      # pause machen und dann refreshen
      QtCore.QTimer.singleShot(time_to_next_round_r,lambda: self.refresh())
	
    def game_over(self):
      print("gameover")
      self.label.setText("Game Over")
      
    def wrong(self):
      #timer stoppen
      self.timer.stop()
      #buttons deaktivieren
      for i in range(0,Anzahl_Antworten):
	self.btnlist[i].setEnabled(False)
	
      print("wrong")
      self.label.setText("WRONG -1")
      
      self.lives=self.lives-1
      if self.lives < 0:
	self.game_over()
      else:
	#zeitänderung wegen wrong
	self.time=self.time*wrongfaktor
	
	#pause machen und dann refreshen
	QtCore.QTimer.singleShot(time_to_next_round_w,lambda: self.refresh())
	  
      
    def refresh(self, first=False):
      #richtige antwort zufällig wählen
      right = random.randint(0, len(answers) )
      #frage setzen
      self.lebenlabel.setText("lives:" + str(self.lives))
      self.label.setText(questions[right])
      #button für richtige antwort zufälig wählen
      r=random.randint(0, Anzahl_Antworten)# -1 entfernt weil letzter button nie right
      print("refresh"+ str(r))
      for i in range(0, Anzahl_Antworten):
	print("refreshdbg1")
	if i == r:
	  print("refreshdbg2")
	  if first != True:
	    print("refreshdbg3")
	    self.btnlist[i].clicked.disconnect()
	  print("refreshdbg4 i= " +str(i))
	  self.btnlist[i].clicked.connect(lambda: self.right())
	  print("refreshdbg13")
	  self.btnlist[i].setText(answers[right])
	  print("refreshdbg14")
	else:
	  print("refreshdbg5")
	  if first != True:
	    print("refreshdbg6")
	    self.btnlist[i].clicked.disconnect()
	  print("refreshdbg7")
	  self.btnlist[i].clicked.connect(lambda: self.wrong())
	  #zufällige antwort != richtige antwort wählen und auf button schreiben 
	  print("refreshdbg8")
	  wrong=random.randint(0,len(answers))#-1)
	  if wrong==right:
	      print("refreshdbg9")
	      if wrong+1 < len(answers):
		print("refreshdbg10")
		wrong=wrong+1
	      else:
		print("refreshdbg11")
		wrong=wrong-1
	  print("refreshdbg12 lenth(answers):" +str(len(answers)) +" i:" + str(i))
	  self.btnlist[i].setText(answers[wrong])
	
	if first != True:  
	  #counter starten wenn nicht der erste aufruf( timer startet nach erster antwort #nachher vieleicht abändern)
	  self.counter=self.time
	  self.timelabel.setText(str(self.time))
	  
	  self.timer.start(100)
	for i in range(0,Anzahl_Antworten):
	  self.btnlist[i].setEnabled(True)

	  
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

      
class StretchedLabel(QtGui.QLabel):
  
  ''' Label dessen Schrift sich mitskaliert
  von: http://stackoverflow.com/questions/8796380/automatically-resizing-label-text-in-qt-strange-behaviour
  so thx to reclosedev, even if he will probably never see this program '''
  
  def __init__(self, *args, **kwargs):
    QtGui.QLabel.__init__(self, *args, **kwargs)
   # self.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)

  def resizeEvent(self, evt):
    font = self.font()
    font.setPixelSize(self.height() * 0.5)
    self.setFont(font)      

class StretchedButton(QtGui.QToolButton):
  
  ''' Button mit skalierender Schrift'''
  
  def __init__(self, *args, **kwargs):
    QtGui.QToolButton.__init__(self, *args, **kwargs)
   # self.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)

  def resizeEvent(self, evt):
    font = self.font()
    font.setPixelSize(self.height() * 0.2)
    self.setFont(font)      
      
      
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
