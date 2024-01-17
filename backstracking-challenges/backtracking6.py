"""
Given a set[] of non-negative integers and a value sum, 
the task is to print the subset of the given set whose sum is equal to the given sum.
"""

def calcSubset(A, res, subset, index, sum):
    # Add the current subset to the result list
    res.append(subset[:])
    
    temp = 0
    for i in range(len(subset)):
        temp += subset[i]
    
    if sum == temp:
        print("il sottoinsieme che equivale la somma è " + str(subset[:]))
 
    # Generate subsets by recursively including and excluding elements
    for i in range(index, len(A)):
        # Include the current element in the subset
        subset.append(A[i])
 
        # Recursively generate subsets with the current element included
        calcSubset(A, res, subset, i + 1, sum)
 
        # Exclude the current element from the subset (backtracking)
        subset.pop()

def subsets(A, sum):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index, sum)
    return res

set = [1,2,3]

sum = 5

print(subsets(set, sum))

# Complexity O(2^n)


