# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:34:33 2017
problem : https://www.hackerrank.com/challenges/qheap1
@author: nanil
"""

#%%
import collections
import math
class MyHeap():
    
    def _init_(self):
        self.heapData = collections.deque()
    
    def AddItem(self,item):
        self.heapData.append(item)
        childNode = len(self.heapData) - 1
        while(childNode > 0):
            parentNode = math.ceil(childNode/2) - 1
            if(self.heapData[parentNode] > self.heapData[childNode]):
                temp = self.heapData[parentNode]
                self.heapData[parentNode] = self.heapData[childNode]
                self.heapData[childNode] = temp
                
                childNode = parentNode
            else:
                break
    
    def DeleteItem(self,item):
        #find the item
        for i in self.heapData:
            if(i == item):
                parentNode = i
                break
        #swap item with the last item
        length = len(self.heapData) - 1
        temp = self.heapData[parentNode]
        self.heapData[parentNode] = self.heapData[length]
        self.heapData[length] = temp
        #remove the item to be deleted
        self.heapData.pop()                
        #now we have to balance the heap
        child1_Node = 2(parentNode) + 1
        child2_Node = 2(parentNode) + 2
        
        while(child1_Node <= length):
            child1 = self.heapData[child1_Node]
            if(child2_Node <= length):
                child2 = self.heapData[child2_Node]
                if(child2 > child1):
                    smallerChildNode = child1_Node
                else:
                    smallerChildNode = child2_Node
            else:
                smallerChildNode = child1_Node
            
            temp = self.heapData[parentNode]
            self.heapData[parentNode] = self.heapData[smallerChildNode]
            self.heapData[smallerChildNode] = temp
            
            parentNode = smallerChildNode
            child1_Node = 2(parentNode) + 1
            child2_Node = 2(parentNode) + 2


queryCountString = input()
queryCount = int(queryCountString)

heap = MyHeap()

