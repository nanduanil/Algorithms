# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:22:37 2017

@author: Nandu Anil
"""
#%%
def QuickSort(unSortedArray):
    global countOfComparison
    pivot = int(unSortedArray[0])

    i = 0
    j = 1
    n = len(unSortedArray)
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
    if(i > 0):
        countOfComparison = countOfComparison + i
        unSortedArray[0:i] = QuickSort(unSortedArray[0:i])
    if(i<(n-1)):
        countOfComparison = countOfComparison + (n - i - 1)
        unSortedArray[i+1:n] = QuickSort(unSortedArray[i+1:n])
        
    return unSortedArray

#%%
unsortedFile = open("QuickSort_1.txt")
intArray = unsortedFile.read().splitlines()

countOfComparison = 0
intArray = QuickSort(intArray)
print("Count Of Comparisions:",countOfComparison)

outfile = open("Sorted.txt",'w')
for line in intArray:
        outfile.write(line + "\n")

unsortedFile.close()
outfile.close()        