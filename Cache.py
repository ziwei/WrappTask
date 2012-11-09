#!/usr/bin/python
import urllib2
import re
import json
import sys
import time

logfile = open("cache", "a")

for i in range(3501, 3889) :
 command = "http://playground.wrapp.com/logs/" + str(i)
 success = False
 while success == False :
  try :
   data = urllib2.urlopen(command).read()
   logfile.write(data)
   success = True
  except :
   time.sleep(3)
#print str(data)
