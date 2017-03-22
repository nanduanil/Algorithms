# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 13:56:24 2017
https://www.hackerrank.com/challenges/dijkstrashortreach
@author: nanil
"""
#==============================================================================
# from heapq import heappush, heappop
# import itertools
# inArray = [line.rstrip('\n') for line in open('C:\\Users\\nandu\\Desktop\\Algorithms\\HackerRank\\Algo\\dijk_shortestReach\\dijk_in01.txt')]
# testCases = int(inArray[0])
# line = 1
# for t in range(0,testCases):
#     counter = itertools.count()
#     command = [int(x) for x in inArray[line].strip().split()]
#     line = line + 1
#     numberOfNodes = command[0]
#     graph = {}
#     for c in range(0,command[1]):
#         nodeData = [int(y) for y in inArray[line].strip().split()]
#         line = line + 1
#         fromNode = nodeData[0]
#         toNode = nodeData[1]
#         weight = nodeData[2]
#         if(fromNode not in graph):
#             graph[fromNode] = []
#         if(toNode not in graph):
#             graph[toNode] = []
#         graph[fromNode].append([toNode,weight])
#         graph[toNode].append([fromNode,weight])
#     nextNode = int(inArray[line])
#     line = line + 1  
#==============================================================================
from heapq import heappush, heappop
import itertools
testCases = int(input())

for t in range(0,testCases):
    counter = itertools.count()
    command = [int(x) for x in input().strip().split()]
    numberOfNodes = command[0]
    graph = {}
    for c in range(0,command[1]):
        nodeData = [int(y) for y in input().strip().split()]
        fromNode = nodeData[0]
        toNode = nodeData[1]
        weight = nodeData[2]
        if(fromNode not in graph):
            graph[fromNode] = []
        if(toNode not in graph):
            graph[toNode] = []
        graph[fromNode].append([toNode,weight])
        graph[toNode].append([fromNode,weight])
    nextNode = int(input())

    startNode = nextNode    
    removed = "REMOVED"
    crossHeap = []
    presentInHeap = {}
    explored = {}
    explored[nextNode] = 0
    for i in range(0,numberOfNodes):
        if(nextNode == -1): break
        currentDistance = explored[nextNode]
        for nodeData in graph[nextNode]:
            toNode = nodeData[0]
            distance = currentDistance+nodeData[1]
            if(toNode not in explored):
                newEntry = [distance,next(counter),toNode]
                if(toNode not in presentInHeap):
                    heappush(crossHeap,newEntry)
                    presentInHeap[toNode] = newEntry
                else:
                    if(presentInHeap[toNode][0] > distance):
                        presentInHeap[toNode][2] = removed
                        heappush(crossHeap,newEntry)
                        presentInHeap[toNode] = newEntry
        del graph[nextNode]
        if(len(crossHeap) == 0): break
        nextNode = -1
        while(True):
            if(len(crossHeap) == 0): break
            nextEntry = heappop(crossHeap)
            if(nextEntry[2] != removed):
                nextNode = nextEntry[2]
                explored[nextNode] = nextEntry[0]
                del presentInHeap[nextEntry[2]]
                break
            
    for i in range(1,numberOfNodes+1):
        if(i==startNode):continue
        if(i in explored):
            print(explored[i],end=" ")
        else:
            print(-1,end=" ")
    print("")
            
            

                