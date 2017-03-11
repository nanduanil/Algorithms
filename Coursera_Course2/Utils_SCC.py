
def ReadFileToDict(fileName,isRev):
    """
    Read the graph data from file into a dictionary
    """
    graph = {}
    with open(fileName) as inFile:
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
            #Makes sure that, even if node is a sink it has an entry
            if(toNode not in graph):
                graph[toNode] = []
    return graph

def ReadFileToDictRev(fileName,isRev):
    """
    Read the graph data from file into a dictionary in reverse order.
    """
    graph = {}
    with open(fileName) as inFile:
        for line in inFile:
            nodeData =[int(i) for i in line.split()]
            fromNode = nodeData[1]
            toNode = nodeData[0]
            if(fromNode in graph):
                #assuming here that the input data does not contain repetition
                graph[fromNode].append(toNode)
            else:
                #create new entry in dictionary
                graph[fromNode] = [toNode]
            #Makes sure that, even if node is a sink it has an entry
            if(toNode not in graph):
                graph[toNode] = []
    return graph

"""
This function finds all nodes findable from the node provided.
Also identifies the running time order.
"""
def DFS_Recursive(graph,currentNode,explored_global,currentNodeTime):
    explored_global[currentNode] = None
    print(currentNode)
    for node in graph[currentNode]:
        if(node not in explored_global):
            DFS_Recursive(graph,node,explored_global,currentNodeTime)
    explored_global[currentNode] = currentNodeTime[0]
    currentNodeTime[0] = currentNodeTime[0] - 1
    return

import collections
"""
This function finds all nodes findable from the node provided.
Also identifies the running time order.
"""
def DFS_RunningTime_Iterative(graph,startNode,explored_global,currentNodeTime):
    popped = {}
    workerQueue = collections.deque()
    workerQueue.append(startNode)
    explored_global[startNode] = None
    while(len(workerQueue) > 0):
        currentNode = workerQueue.pop()
        if(currentNode in popped):
            explored_global[currentNode] = currentNodeTime[0]
            currentNodeTime[0] = currentNodeTime[0] - 1
            continue
        else:
            popped[currentNode] = None
            workerQueue.append(currentNode)
        for node in graph[currentNode]:
            if(node not in explored_global): 
                explored_global[node] = None
                workerQueue.append(node)

"""
This function finds all nodes findable from the node provided.
It returns the nodes found.
"""
def DFS_SCC_Iterative(graph,startNode,explored_global):
    popped = {}
    workerQueue = collections.deque()
    workerQueue.append(startNode)
    explored_global[startNode] = None
    while(len(workerQueue) > 0):
        currentNode = workerQueue.pop()
        if(currentNode in popped):
            explored_global[currentNode] = True
            continue
        else:
            popped[currentNode] = None
            workerQueue.append(currentNode)
        for node in graph[currentNode]:
            if(node not in explored_global): 
                explored_global[node] = None
                workerQueue.append(node)
    return popped
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                