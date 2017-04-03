# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:18:28 2017

@author: nandu
"""
#%%
from heapq import heappush,heappop

#max heap is maintained by storing the values as negetive of the actual value
leftMaxHeap = []
rightMinHeap = []
lenLeftHeap = 0
lenRightHeap = 0
m = 0

inputArray = [int(line.strip()) for line in open('Median.txt')]
#inputArray = [int(line.strip()) for line in open('C:\\Users\\nandu\\Desktop\\Algorithms\\Coursera_Course2\\MedianMaintenance_Heap\\test1.txt')]

#initialize the right heap with the first value
rightMinHeap = [inputArray[0]]
lenRightHeap = 1

#first median is also the first value
m = inputArray[0]

for newItem in inputArray[1:]:    
    #if the next item is lesser than the minimum from right array
    if(newItem < rightMinHeap[0]):
        
        #place item into left array
        heappush(leftMaxHeap,(newItem * -1))
        
        #if right array was greater than the left no need to do any adjustment    
        if(lenRightHeap>lenLeftHeap):
            lenLeftHeap += 1
            newMedian = (leftMaxHeap[0] * -1)
        #else, after current insert left array count would be more than right one
        #so, pop one item from left to right array
        else:
            heappush(rightMinHeap,(heappop(leftMaxHeap) * -1))
            lenRightHeap += 1
            newMedian = rightMinHeap[0]
            
    #if next item is greater than or equal to minimum from right heap
    else:
        #place item into right array
        heappush(rightMinHeap,newItem)
        
        #if right array was greater than the left, then 
        #after the current insert right array count would be more than left 
        #by two count.
        #so, pop one item from right to left array
        if(lenRightHeap>lenLeftHeap):          
            heappush(leftMaxHeap,(heappop(rightMinHeap) * -1))           
            lenLeftHeap += 1
            newMedian = (leftMaxHeap[0] * -1)
        #if right array was same length as the left no need to do any adjustment 
        else:
            lenRightHeap += 1
            newMedian = rightMinHeap[0]
    m = m + newMedian
print(m%10000)