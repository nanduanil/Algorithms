# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:53:43 2017

@author: nandu
"""
#%%

#countOfInverse = 0
def FindInv(file):
    intFile = open(file)
    intList = intFile.read().splitlines()
    print(len(intList))
    countOfInverse = 0
    intList.append(countOfInverse)
        #input[i:i+n] for i in range(0, len(input), n)
    intList = recurseFindInversion(intList)
    print("Count of inverse:",intList.pop(-1))
    outfile = open("blah.txt",'w')
    print(len(intList))
    for line in intList:
        outfile.write(line + "\n")
    #print("Sorted List:",intList)
    intFile.close()
    
    
#%% 
def recurseFindInversion(intList):
    countOfInverse = intList.pop(-1)
    if(len(intList) > 1):
        splitLenList = len(intList)//2
        intList1 = intList[0:splitLenList]
        intList2 = intList[splitLenList:]
        
        intList1.append(countOfInverse)
        
        if(len(intList1) > 1):
            intList1 = recurseFindInversion(intList1)
        
        countOfInverse = intList1.pop(-1)
        intList2.append(countOfInverse)
        
        if(len(intList2) > 1):
            intList2 = recurseFindInversion(intList2)
        
        countOfInverse = intList2.pop(-1)
        intListSorted = []
        
        while (len(intList1) > 0 and len(intList2) > 0):
            if(int(intList1[0]) <= int(intList2[0])):
                intListSorted.append(intList1.pop(0))
            elif(int(intList1[0]) > int(intList2[0])):
                intListSorted.append(intList2.pop(0))
                countOfInverse = countOfInverse + len(intList1)
            
        if(len(intList1) > 0):
            intListSorted.extend(intList1)
        if(len(intList2) > 0):
            intListSorted.extend(intList2)
            
        intListSorted.append(countOfInverse)
        return intListSorted
        
    else:
        intList.append(countOfInverse)
        return intList

    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    