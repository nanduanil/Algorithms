# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:04:35 2017
"""

inputArray = [line.strip() for line in open('jobs.txt')]
count = int(inputArray[0])

jobData_1 = []
jobData_2 = []
for inputData in inputArray[1:]:
    weight,time = [int(x) for x in inputData.split()]
    jobData_1.append([(weight-time), weight, time])
    jobData_2.append([(weight/time), weight, time])
            
import operator
jobSorted_1  = sorted(jobData_1, key=operator.itemgetter(0,1), reverse = True)
jobSorted_2  = sorted(jobData_2, key=operator.itemgetter(0,1), reverse = True)

weightCompletion = 0
completionTime = 0
for job in jobSorted_1:
    completionTime = completionTime + job[2]
    weightCompletion = weightCompletion +  (job[1] * completionTime)


print("weight Completion using (weight - runnningTime)",weightCompletion)

weightCompletion = 0
completionTime = 0
for job in jobSorted_2:
    completionTime = completionTime + job[2]
    weightCompletion = weightCompletion +  (job[1] * completionTime)

print("weight Completion using (weight/runnningTime)",weightCompletion)