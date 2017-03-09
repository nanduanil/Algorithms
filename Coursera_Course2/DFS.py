"""
Created on Thurs Mar  9
@author: Nandu Anil
"""

import collections
def DFS_Iterative(graph,startNode):
    explored = {}
    workerQueue = collections.deque()
    workerQueue.append(startNode)
    explored[startNode] = True
    while(len(workerQueue) > 0):
        currentNode = workerQueue.pop()
        print(currentNode)
        if(currentNode not in graph):
            continue
        for node in graph[currentNode]:
            if(node not in explored): 
                explored[node] = True
                workerQueue.append(node)         
    return explored  


def DFS_Recursive(graph,currentNode,explored_global):
    explored_global[currentNode] = True
    print(currentNode)
    if(currentNode not in graph):
        return
    for node in graph[currentNode]:
        if(node not in explored_global):
            DFS_Recursive(graph,node,explored_global)
     


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
explored_global = {}
print("-- Nodes Explored --")
DFS_Recursive(graph,startNode,explored_global)
print("Done")
