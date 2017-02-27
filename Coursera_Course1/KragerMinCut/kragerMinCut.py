# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:48:57 2017

@author: nandu
"""
#%%
import random
def minCut(graphDict):

    random.seed()
    while (len(graphDict.keys()) > 2):
        firstNodeKey = random.choice(list(graphDict.keys()))
        secondNodeKey = random.choice(graphDict[firstNodeKey])
        
        newNodeKey = firstNodeKey + ',' + secondNodeKey
        
        newNodeAdjacency =  graphDict[firstNodeKey] + graphDict[secondNodeKey]
        popList = []
        for adj in range(0,len(newNodeAdjacency)):
            if(newNodeAdjacency[adj] == firstNodeKey or newNodeAdjacency[adj] == secondNodeKey):
                popList.append(adj)
        for i in reversed(popList):
            newNodeAdjacency.pop(i)
            
        graphDict[newNodeKey] = newNodeAdjacency
        del graphDict[firstNodeKey]
        del graphDict[secondNodeKey]
        
        for updateAdj in graphDict[newNodeKey]:
            updateAdjList = graphDict[updateAdj]
            for a in range(0,len(updateAdjList)):
                if(updateAdjList[a] == firstNodeKey or updateAdjList[a] == secondNodeKey):
                    updateAdjList[a] = newNodeKey
            graphDict[updateAdj] = updateAdjList
        
    return graphDict
#%%
import random
import copy
import time
inputGraph = open("kargerMinCut.txt")

graphDictOrig = {}
graphDictIterationInput = {}
graphDictIterationOutput = {}
graphDictIterationMinOutput = {}

for stringRow in inputGraph.read().splitlines():
    graphRow = [str(i) for i in stringRow.split()]
    graphDictOrig[graphRow[0]] = graphRow[1:]

graphDictIterationInput = copy.deepcopy(graphDictOrig)

graphDictIterationOutput = minCut(graphDictIterationInput)
keysOutput = list(graphDictIterationOutput.keys())
minimumCut = len(graphDictIterationOutput[keysOutput[0]])
#uncomment all 'graphDictIterationMinOutput' lines to get the split which has the minimum cut
#graphDictIterationMinOutput = copy.deepcopy(graphDictIterationOutput)
n = len(graphDictOrig)
start = time.time()
for i in range(0,20):
    graphDictIterationInput = {}
    graphDictIterationOutput = {}
    graphDictIterationInput = copy.deepcopy(graphDictOrig)
    graphDictIterationOutput = minCut(graphDictIterationInput)
    keysOutput = list(graphDictIterationOutput.keys())
    if(minimumCut > len(graphDictIterationOutput[keysOutput[0]])):
        minimumCut = len(graphDictIterationOutput[keysOutput[0]])
        #graphDictIterationMinOutput = {}
        #graphDictIterationMinOutput = copy.deepcopy(graphDictIterationOutput)
    
end = time.time()
print("time taken:",end-start)
print("minimum Cut: ", minimumCut)
#%%
    


         
