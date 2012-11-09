#!/usr/bin/python
import re
import sys

import ReadLog

restrict = 5000
contributedList = []
contdistribution = []
totaldistribution = []
logList = ReadLog.ReadLog()
#print str(len(logList))
#print str(campaignsforlist)
#print str(reservegiftlist)

for indexR in range(1, len(logList)) :
 if len(logList[indexR]) == 2 :
  indexC = indexR - 1
  if indexR - restrict >= 0 :
   boundary = indexR - restrict
  else :
   boundary = 0
  while (indexC >= boundary) :
   if len(logList[indexC]) == 3 :
    if logList[indexR][0] == logList[indexC][0] :
     if logList[indexR][1] in logList[indexC][1] :
      contributedList.append(logList[indexC][2])
      break
   indexC = indexC - 1

#print str(contributedList)

#strategies = set()
strategies = []
for i in range(0, len(contributedList)) :
 if contributedList[i] in strategies :
  indexS = strategies.index(contributedList[i])
  contdistribution[indexS] = contdistribution[indexS] + 1
 else :
  strategies.append(contributedList[i])
  contdistribution.append(1)
  totaldistribution.append(0)

for i in range(0, len(logList)) :
 if len(logList[i]) == 3 :
  indexS = strategies.index(logList[i][2])
  totaldistribution[indexS] = totaldistribution[indexS] + 1
  

print str(strategies)
print str(contdistribution)
print str(totaldistribution)
for i in range(0, len(strategies)) :
 print str(strategies[i]) + " : " + str(float(contdistribution[i])/float(totaldistribution[i]))
