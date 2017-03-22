# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:59:22 2017

@author: nandu
"""
from heapq import heappush, heappop
import Utils_dij
import itertools
inputFile = "dijkstraData.txt"
#inputFile = "dijk2.txt"
graph,notExplored = Utils_dij.ReadFileToDict(inputFile)

notReachable = 1000000
explored = {}
length = len(graph)
crossingEdgeHeap = []
nodesInCrossing = {}
removedNode = -1
selectedNode = 1

explored[1] = 0
notExplored.pop(selectedNode)
counter = itertools.count()
for i in range(0,length):
    #Utils_dij.UpdateCrossingEdges(graph,previousNode,selectedNode,explored,notExplored,crossingEdges,nodesInCrossing)
    for node in graph[selectedNode]:
        baseDistance = explored[selectedNode]
        possibleNode = node[0]
        if(possibleNode in explored):
            continue
        newCrossing = [baseDistance+node[1],next(counter),possibleNode]
        if(possibleNode not in nodesInCrossing):
            heappush(crossingEdgeHeap,newCrossing)
            nodesInCrossing[possibleNode] = newCrossing
        else:
            if(nodesInCrossing[possibleNode][0] > newCrossing[0]):
                removeNode = nodesInCrossing.pop(possibleNode)
                removeNode[-1] = removedNode
                heappush(crossingEdgeHeap,newCrossing)
                nodesInCrossing[possibleNode] = newCrossing
    selectedNode = removedNode
    while(True):
        if(len(crossingEdgeHeap) == 0):
            break
        nextNodeEntry = heappop(crossingEdgeHeap)
        selectedNode = nextNodeEntry[2]    
        if(selectedNode != removedNode):
            break
    if(selectedNode == removedNode):
        break
    explored[selectedNode] = nextNodeEntry[0]
    notExplored.pop(selectedNode)

for e in notExplored:
    explored[e] = notReachable

outputNodes = [7,37,59,82,99,115,133,165,188,197]

for out in outputNodes:
    print(explored[out],end=',')
    
    
    
    