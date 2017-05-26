# -*- coding: utf-8 -*-
"""
Created on Wed May 24 22:57:18 2017
"""

#read input data
inputArray = [line.strip() for line in open('edges.txt')]
numOfNodes,numOfEdges = [int(x) for x in inputArray[0].split()]

#edge data as adjacency list                         
edges = {}
#status track on the vertex.
vertexStatus = {}
heapInput = []
from heapq import heappop,heappush
for i in inputArray[1:]:
    v1,v2,weightStr = i.split()
    weight = int(weightStr)
    
    if(v1 not in edges):
        edges[v1] = {}
        entry = [10000,v1]    
        heapInput.append(entry)
        vertexStatus[v1] = entry 
    if(v2 not in edges):
        edges[v2] = {}
        entry = [10000,v2]
        heapInput.append(entry)
        vertexStatus[v2] = entry
    edges[v1][v2] = weight
    edges[v2][v1] = weight


minSpanning = 0
count = 0
heapInput[0][0] = 0
#continue running until there is a vertex in the heap
while(len(heapInput) > 0):
    #choose vertex with the minimum edge with vertices already chosen
    chosenVertex = heappop(heapInput)[1]
    #if this vertex has already been chosen then continue
    if(chosenVertex == 'REMOVED'):
        continue
    #remove the vertex details from the status dictionary
    vStatus = vertexStatus.pop(chosenVertex)
    #if the vertex edge is 10000 then there is no connection to the chosen vertices
    if(vStatus[0] == 10000):
        print("graph is not connected.")
        break
    
    minSpanning = minSpanning + vStatus[0]
    count = count +1
    
    #update edge costs of new edges crossing from chosen to unchosen
    for v in edges[chosenVertex]:
        currentWeight = edges[chosenVertex][v]
        #if v is already chosen
        if(v not in vertexStatus):
            continue
        vStatus = vertexStatus[v]
        #if edge cost of this vertex is smaller than previous crossing edge for the same vertex
        #mark old entry in the heap as 'REMOVED'. This facilitates lazy deletion from heap
        #push entry with updated edge cost into the heap.
        if(vStatus[0] > currentWeight):
            newEntry = [currentWeight,v]
            vStatus[1] = 'REMOVED'
            heappush(heapInput,newEntry)
            vertexStatus[v] = newEntry

print("Minimum Spanning Tree:", minSpanning)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    