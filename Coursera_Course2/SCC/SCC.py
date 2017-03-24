import Utils_SCC
import time

#inputFile = "scc1.txt"
inputFile = "SCC.txt"

#read the graph data from file
start_time = time.time()
normGraph = Utils_SCC.ReadFileToDict(inputFile,False)
print("--- %s seconds ---" % (time.time() - start_time))

#read the graph data in reverse order
start_time = time.time()
revGraph = Utils_SCC.ReadFileToDictRev(inputFile,True)
print("--- %s seconds ---" % (time.time() - start_time))

runningTime = {}
start_time = time.time()
currentNodeTime = [len(normGraph)]
start_time = time.time()
#calculate the running time data of each node using DFS
for i in revGraph:
    if(i not in runningTime):    
        Utils_SCC.DFS_RunningTime_Iterative(revGraph,i,runningTime,currentNodeTime)
        #Utils_SCC.DFS_Recursive(revGraph,i,runningTime,currentNodeTime)
print("---[for finding Running Time] %s seconds ---" % (time.time() - start_time))

#use the running time parameter to find SCC's
explored={}
start_time = time.time()        
SCC_size = []
for node in sorted(runningTime, key=runningTime.get, reverse=False):
    if(node not in explored):
        nodesFound = None
        #nodesFound are the SCC's in the graph
        nodesFound = Utils_SCC.DFS_SCC_Iterative(normGraph,node,explored)
        SCC_size.append(len(nodesFound))
print("--- [For finding SCC]%s seconds ---" % (time.time() - start_time))     

#sort the SCC's from largest to smallest
sccSizeSorted = sorted(SCC_size,key=None,reverse=True)
print(sccSizeSorted[0:10])
#print(runningTime)