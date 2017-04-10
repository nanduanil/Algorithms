# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 22:50:21 2017

@author: nandu
"""
import time

startTime = time.time()
inputNumbers = {}
inputArray = []
for line in open('2sum.txt'):
    newNum = int(line)
    if(newNum in inputNumbers):
        inputNumbers[newNum] = True
    else:
        inputNumbers[newNum] = False
    inputArray.append(newNum)        
length = len(inputNumbers)

print(time.time() - startTime)
startTime = time.time()

reqValues = {}
for i in  range(-10000,-9900):
    reqValues[i] = True

countOfRequired = 0
for num in inputArray:
    foundValues = []
    for t in reqValues:
        reqNum = t - num     
        if(reqNum in inputNumbers):
            if(reqNum == num and inputNumbers[num] == False):
                continue
            countOfRequired += 1
            foundValues.append(t)    
    for key in foundValues:
        reqValues.pop(key,None)
    
print(time.time() - startTime)
print(countOfRequired)


