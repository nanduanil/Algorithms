import Utils_SCC
import time

inputFile = "bfs_input1.txt"
inputFile = "SCC.txt"

start_time = time.time()
normGraph = Utils_SCC.ReadFileToDict(inputFile,False)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
revGraph = Utils_SCC.ReadFileToDictRev(inputFile,True)
print("--- %s seconds ---" % (time.time() - start_time))

#print(normGraph)
#print(revGraph)

runningTime = {}
start_time = time.time()
currentNodeTime = [len(normGraph)]
start_time = time.time()
#DFS_Recursive(revGraph,5,explored_global,currentNodeTime)
for i in revGraph:
    if(i not in runningTime):    
        Utils_SCC.DFS_RunningTime_Iterative(revGraph,i,runningTime,currentNodeTime)
print("---[for finding Running Time] %s seconds ---" % (time.time() - start_time))

explored={}
start_time = time.time()        
SCC_size = []
for node in sorted(runningTime, key=runningTime.get, reverse=True):
    if(node not in explored):
        nodesFound = None
        nodesFound = Utils_SCC.DFS_SCC_Iterative(normGraph,node,explored)
        SCC_size.append(len(nodesFound))
       
print("--- [For finding SCC]%s seconds ---" % (time.time() - start_time))     
print("--- %s seconds ---" % (time.time() - start_time))


sccSizeSorted = sorted(SCC_size,key=None,reverse=True)
print(sccSizeSorted[0:10])
#print(runningTime)