# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 20:48:57 2017

@author: nandu
"""
#%%
import random
inputGraph = open("kargerMinCut.txt")

graphDict = {}
for stringRow in inputGraph.read().splitlines():
    graphRow = [str(i) for i in stringRow.split()]
    graphDict[graphRow[0]] = graphRow[1:]



graphDict = minCut(graphDict)

#%%
    

import random
def minCut(graphDict):

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
         
