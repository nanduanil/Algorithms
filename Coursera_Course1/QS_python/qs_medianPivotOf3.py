# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:22:37 2017

@author: Nandu Anil

This script takes the pivot position as parameter
"""
#%%
def FindPivot(inputArray):
    import statistics
    import math
     
    middleIndex = (math.ceil(len(inputArray)/2) - 1)
    medianArray = [int(inputArray[0]),int(inputArray[middleIndex]),int(inputArray[-1])]
    #medianArray = [(inputArray[0]),(inputArray[middleIndex]),(inputArray[-1])]
    medianElement = statistics.median(medianArray)
    print("medianArray",medianArray)
    print("medianElement",medianElement)
    if(medianArray[0]==medianElement):
        positionOfPivot = 0
    elif(medianArray[1]==medianElement):
        positionOfPivot = middleIndex
    elif(medianArray[2]==medianElement):
        positionOfPivot = -1
    else:
        positionOfPivot = 0
    print("pivot position",positionOfPivot)
    return positionOfPivot

#%%
def QuickSort(unSortedArray):
    
    global countOfComparison
    n = len(unSortedArray)
    
    positionOfPivot = FindPivot(unSortedArray)
    temp = unSortedArray[positionOfPivot]
    unSortedArray[positionOfPivot] = unSortedArray[0]
    unSortedArray[0] = temp
    
    pivot = int(unSortedArray[0])
    
    i = 0
    j = 1
    print("array before partition:",unSortedArray)
    #j loops from 1 to n-1 so n-2 loops
    for item in range(0,n-1):
        if(int(unSortedArray[j]) >= pivot):
            j = j + 1
        elif(int(unSortedArray[j]) < pivot):
            temp = unSortedArray[j]
            unSortedArray[j] = unSortedArray[i+1]
            unSortedArray[i+1] = temp
            j = j + 1
            i = i + 1
    #swap pivot to correct location
    unSortedArray[0] = unSortedArray[i]
    unSortedArray[i] = str(pivot)
    print("array after partition:",unSortedArray)
    if(i > 0):
        countOfComparison = countOfComparison + i - 1
        print("increment small:",i - 1)
        unSortedArray[0:i] = QuickSort(unSortedArray[0:i])
    if(i<(n-1)):
        countOfComparison = countOfComparison + (n - i - 2)
        print("increment large:",(n - i - 2))
        unSortedArray[i+1:n] = QuickSort(unSortedArray[i+1:n])
        
    return unSortedArray
#%%

unsortedFile = open("QuickSort_1.txt")
intArray = unsortedFile.read().splitlines()
#intArray = ['8','2','24','5','7','1']
countOfComparison = len(intArray) - 1
intArray = QuickSort(intArray)
print("Count Of Comparisions:",countOfComparison)

outfile = open("Sorted.txt",'w')
for line in intArray:
        outfile.write(line + "\n")

unsortedFile.close()
outfile.close()        