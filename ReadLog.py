#!/usr/bin/python
import urllib2
import re
import json
import sys
import time

'''for i in range(0, 30) :
 command = "http://playground.wrapp.com/logs/" + str(i)
 success = False
 while success == False :
  try :
   data = urllib2.urlopen(command).read()
   success = True
  except :
   time.sleep(3)'''
#print str(data)

#campaignsforlist = []
#reservegiftlist = []
def ReadLog() :
 logList = []
 for line in open("cache","r") :
  #prefix = line.split(":")[0]
  #date = prefix.split("-")[1]
  jCode = '{' + line.split('{')[1]
  jObj = json.loads(jCode)
  #print str(jCode)
  if 'strategy' in jObj :
   strategy = jObj.pop('strategy')
   #if strategy != None : 
   if 'sender_id' in jObj :
    sender_id = jObj.pop('sender_id')
    if 'campaigns' in jObj :
     campaigns = jObj.pop('campaigns')
    elif 'campaigns:' in jObj :
     campaigns = jObj.pop('campaigns:')
    else :
     campaigns = []
    logList.append((sender_id, campaigns, strategy))
  elif 'user' in jObj :
    user = jObj.pop('user')
    campaign = jObj.pop('campaign')
    logList.append((user, campaign))
 #reservegiftlist = sorted(reservegiftlist, key=lambda reserve: reserve[0])
 #campaignsforlist = sorted(campaignsforlist, key=lambda campaigns: campaigns[0])
 #print str(logList)
 return logList

