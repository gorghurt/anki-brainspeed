#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import threading
class Timer(threading.Thread):
  def __init__(self, seconds):
    self.runTime = seconds
    threading.Thread.__init__(self)
  def run(self):
    time.sleep(self.runTime)
    print "Buzzzz!! Time's up!"

t = Timer(10)
t.start()


class CountDownTimer(Timer):
  def run(self):
    counter = self.runTime
    for sec in range(self.runTime):
      print counter
      time.sleep(1.0)
      counter -= 1
    print "Done."	
c = CountDownTimer(10)
c.start()


class CountDownExec(CountDownTimer):
  def __init__(self, seconds, action):
    self.action = action
    CountDownTimer.__init__(self, seconds)
  def run(self):
    CountDownTimer.run(self)
    self.action()
  def myAction():
    print "Performing my action..."
d = CountDownExec(10, myAction)
d.start()