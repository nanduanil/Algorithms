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
"""

#%%
import collections
def BFS(graph,startNode):
    explored = [False]*len(graph)
    workerQueue = collections.deque(startNode)
    while(len(workerQueue) > 0):
        currentNode = workerQueue.popleft()
        explored[currentNode] = True 
        for node in graph[currentNode]:
            if(explored[node] == False):
                explored[node] = True 
                workerQueue.append(node)  

graph = {}
with open("bfs_input1.txt") as inFile:
    for line in inFile:
        nodeData =[int(i) for i in line.split()]
        fromNode = nodeData[0]
        toNode = nodeData[1]
        if(fromNode in graph):
            graph[fromNode].append(toNode)
        else:
            graph[fromNode] = [toNode]
print(graph) 






        
    
    

    
    
    

