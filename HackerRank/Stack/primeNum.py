# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:08:10 2017
Prime Number using Sieve Of Eratosthenes
@author: nanil
"""
#%%
def findPrime_SOE(upperLimit):
    if(upperLimit < 2):
        return []
    primes = [2,3]
    primesToCheck = []
    possiblePrimes = {}
    if(upperLimit < 5):
        return primes
    for i in range(5,upperLimit,2):
        if(i%3 == 0):
            continue
        possiblePrimes[i] = True
        primesToCheck.append(i)
        
    for j in primesToCheck:
        if(possiblePrimes[j]):
            primes.append(j)
            for k in range(j*j,upperLimit,j):
                if(k in possiblePrimes):
                    possiblePrimes[k] = False
    return primes

#findPrime_SOE(10)