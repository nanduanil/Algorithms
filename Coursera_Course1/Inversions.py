# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:53:43 2017

@author: nandu
"""
#%%

#countOfInverse = 0
#def FindInv():
intFile = open("IntegerArray.txt")
intList = intFile.read().splitlines()
countOfInverse = 0
intList.append(countOfInverse)
    #input[i:i+n] for i in range(0, len(input), n)
intList = recurseFindInversion(intList)
print("Count of inverse:",intList.pop(-1))
print("Sorted List:",intList)
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
        
        countOfInverse = countOfInverse + intList1.pop(-1)
        intList2.append(countOfInverse)
        
        if(len(intList2) > 1):
            intList2 = recurseFindInversion(intList2)
        
        countOfInverse = countOfInverse + intList2.pop(-1)
        intList = []
        
        while (len(intList1) > 0 and len(intList2) > 0):
            if(intList1[0] >= intList2[0]):
                intList.append(intList1.pop(0))
            elif(intList1[0] < intList2[0]):
                intList.append(intList2.pop(0))
                countOfInverse = countOfInverse + len(intList1)
            
        if(len(intList1) > 0):
            intList.extend(intList1)
        if(len(intList2) > 0):
            intList.extend(intList2)
            
        intList.append(countOfInverse)
        return intList
        
    else:
        intList.append(countOfInverse)
        return intList

    

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    