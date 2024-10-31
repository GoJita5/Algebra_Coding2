#---------------------Algebra and Coding Second Homework---------------------------#
    #|########Student: Touer Mohamed Elamine.
    #|##########Group: 4.
    #|##Academic Year: 2024/2025.
    #|######Professor: Rezki Chemlal.
#---------------------Algebra and Coding Second Homework---------------------------#

import numpy as np
import itertools as it
from time import time

#-----------------------------#SOLUTION#-----------------------------#


def mindist(c, n, m): #Computes the minimum distance of a block code of length n, of m codewords.
    dists = []
    for j in range(0, m-1): #Comparing word j to each word after it (i.e. we compare every two words, but without repetition)
        for k in range(j+1, m):
            dists.append(sum(c[j,i] != c[k,i] for i in range(0, n)))
            if 1 in dists:
                return 1
    return min(dists) 


def brutesearch(): #Finds a binary code of length 6 with the highest minimum distance possible (3) using bruteforce.
    #Proposition: every q-ary (n,M,d)-code is equivalent to an (n,M,d)-code that contains (0,0,...,0). Refer to Hill's book.
    combs = list(set(it.combinations([0,0,0,0,0,0,1,1,1,1,1,1], 6))) #All possible combinations of 0's and 1's of length 6, not permuted though.
    #combs.remove((0,0,0,0,0,0)) #Removes (0,0,...,0).
    combs = list(s for s in combs if sum(s) >= 3) #Since our code will contain (0,0,...,0), and d>2, then the weight of each codeword
    #must be >2 (i.e. there must be at least 3 ones in each codeword if we want d>=3)
    combs = list(it.chain.from_iterable(set(it.permutations(i)) for i in combs)) #We add the permutations, we get a set of 42 codewords
    for i in it.combinations(combs, 7):
        if mindist(np.array(i), 6, 7) == 3:
            return [(0,0,0,0,0,0), *i]
        



print("---------------------------------------------------")

g4codes = [np.array([[0,0,0,0,0,0],[0,0,1,1,1,0], [0,1,0,1,1,1],[0,1,1,0,0,1],[1,0,0,0,1,1],[1,1,0,1,0,0],[1,0,1,0,1,1],[1,1,1,0,0,0]]),
                    np.array([[0,0,0,0,0,0],[0,0,1,1,1,1],[0,1,0,1,1,1],[0,1,1,0,1,1],[1,0,0,1,1,1],[1,0,1,1,0,1],[1,1,0,0,0,1],[1,1,1,0,0,0]]),
                    np.array([[1,1,1,0,0,0],[0,1,1,0,0,1],[1,1,0,0,1,0],[0,1,0,0,1,1],[1,0,1,1,0,0],[0,0,1,1,0,1],[1,0,0,1,1,0],[0,0,0,1,1,1]]),
                    np.array([[4,0,3,0,3,1], [4,0,1,0,0,2],[0,1,4,0,2,3],[3,0,1,4,4,1], [4,1,2,0,0,4], [4,1,0,0,2,0], [2,0,2,4,4,3], [2,0,4,4,2,2]])]
for i in range(0,4):
    print("\n###########################\n")
    print(f"Code {i}:")
    print(g4codes[i],"")
    print(f"the minimum distance of code {i} is: {mindist(g4codes[i],6,8)}")
print("\n###########################")
print("\nThe last code has d=3, but it is not a binary code\n")




print("---------------------------------------------------")


print("Finding a binary code C of length 6 and 8 codewords with minimum distance d = 3...",)
t0 = time()
C=brutesearch()
print("Found!\nC =", C)
print("Minimum distance check...\nd(C) =", mindist(np.array(C), 6, 8))
print("Runtime: ", time()-t0)
print(C)
print("---------------------------------------------------")


#Ignore this, it is for testing purposes only:
'''
def mindist2(c, n, m): #Computes the minimum distance of a block code of length n, of m codewords.
    dists = []
    for j in range(0, m-1): #Comparing word j to each word after it (i.e. we compare every two words, but efficiently)
        for k in range(j+1, m):
            dists.append([sum(c[j,i] != c[k,i] for i in range(0, n)), j, k])
            if 1 in dists:
                return 1
    return dists 
'''
'''
A = [(0,0,1), (0,1,1), (1,1,1)]
B = list(it.combinations(A, 2, ))
print(A)
#A = list(it.chain.from_iterable(set(it.permutations(i)) for i in A))
#print(A)
print(B)
z = it.combinations(A,2)
for i in z:
    print(mindist(np.array(i), 3, 2))
'''
