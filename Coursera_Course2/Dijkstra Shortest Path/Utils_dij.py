
def ReadFileToDict(fileName):
    """
    Read the graph data from file into a dictionary
    """
    graph = {}
    notExplored = {}
    with open(fileName) as inFile:
        for line in inFile:
            lineArray = line.split()
            index = int(lineArray[0])
            graph[index] = []
            notExplored[index] = True
            for nodeData in lineArray[1:]:
                graph[index].append([int(i) for i in nodeData.split(',')])
    return graph,notExplored


            



             
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                