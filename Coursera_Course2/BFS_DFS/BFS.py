# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 14:07:57 2017

@author: Nandu Anil
"""

"""
graph = graph in adjacency list format
startNode = Node from which to start BFS. 
            This will be the row number of the node in the graph list.
workerQueue = this needs to be FIFO; using deque type
output : all the explored nodes
"""

#%%
import collections
def BFS(graph,startNode):
    explored = {}
    workerQueue = collections.deque()
    workerQueue.append(startNode)
    explored[startNode] = True
    while(len(workerQueue) > 0):
        currentNode = workerQueue.popleft()
        if(currentNode not in graph):
            continue
        for node in graph[currentNode]:
            if(node not in explored): 
                explored[node] = True
                workerQueue.append(node)         
    return explored  

graph = {1: [2, 3], 2: [4], 3: [6], 4: [6, 5, 3], 6: [7], 7: [5], 8: [9]}
"""
#use this code if taking input from file
graph = {}
with open("bfs_input1.txt") as inFile:
    for line in inFile:
        nodeData =[int(i) for i in line.split()]
        fromNode = nodeData[0]
        toNode = nodeData[1]
        if(fromNode in graph):
            #assuming here that the input data does not contain repetition
            graph[fromNode].append(toNode)
        else:
            #create new entry in dictionary
            graph[fromNode] = [toNode]
#end file input
"""

print(graph)
startNode = int(input("Enter start node: "))

print("-- Nodes Explored --")
for k in BFS(graph,startNode).keys():
    print(k)

 






        
    
    

    
    
    

