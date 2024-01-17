""" 
PROBLEM 2
A sequence of n > 0 integers is called jolly if the absolute values of the differences between consecutive elements encompass
 all values from 1 to n − 1. For example,
1 4 2 3
is a jolly sequence because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence 
composed of a single integer is a jolly sequence. Implement a program to determine whether a given input sequence is a jolly sequence.

INPUT
Each line contains an integer n ≤ 3000, followed by n integers representing the sequence.

OUTPUT
For each input line, generate an output line with the text: "Jolly" or "Not jolly".

Sample Input
4 1 4 2 3
5 1 4 2 -1 6

Sample Output
Jolly
Not jolly
"""
def build_jolly(A):
    n = len(A)
    if n > 3000:
        return ValueError
    is_jolly = find_jolly(A, 0, 1, n)
    if is_jolly:
        print("Jolly")
    else: print("Not Jolly")

def find_jolly(A, now, next, n):
    if now+1 == n:
        is_jolly = True
        return is_jolly
    
    diff = abs(A[now] - A[next])
    if (diff == abs(n - (now+1))) or (diff == abs(n - (now+2))):
        is_jolly = find_jolly(A, now+1, now+2, n)
    else:
        is_jolly = False
    
    return is_jolly
    
A = [11, 7, 4, 2, 1, 6]

build_jolly(A)

# Complexity O(n/2) = O(n)


# ----------------------------------------------------------------------------------------------------
# Variante

# Function to check whether given 
# sequence is Jolly Jumper or not
def isJolly(a, n):

	# Boolean vector to diffSet set 
	# of differences. The vector is 
	# initialized as false.
	diffSet = [False] * n 

	# Traverse all array elements
	for i in range(0, n-1):
	
		# Find absolute difference between
		# current two
		d = abs(a[i]-a[i + 1]) 

		# If difference is out of range or
		# repeated, return false.
		if (d == 0 or d > n-1 or diffSet[d] == True):
			return False

		# Set presence of d in set.
		diffSet[d] = True
	
	return True
	
# Driver Code
a = [11, 7, 4, 2, 1, 6] 
n = len(a) 

print("Yes") if isJolly(a, n) else print("No") 

# This code is contributed by
# Smitha Dinesh Semwal

    

    