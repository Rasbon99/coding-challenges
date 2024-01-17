""" 
PROBLEM 1
Mr. Rossi moves to Naples. He has a very large family in Naples, and they all live on Via Roma. Since he intends to visit all his 
relatives often, he is trying to find a house close to them. Mr. Rossi wants to minimize the total distance from all of them (i.e., 
he wants to determine the optimal position of the house that minimizes the sum of distances from his relatives' houses), and he has 
hired you to write a program to solve the problem.

INPUT

The input consists of several test cases. The first line contains the number of test cases. For each test case, an integer is provided
 indicating the number of relatives r (0 < r < 500), and the street numbers (also integers) s1, s2, ..., si, ..., sr where they live 
 (0 < si < 30000). Note that different relatives might live at the same street number.

OUTPUT

For each test case, the program outputs the minimum sum of distances from Mr. Rossi's house to each of his relatives' houses. 
The distance between two street numbers si and sj is dij = |si − sj|.

Sample Input

2
2 2 4
3 2 4 6

Sample Output

2
4
"""
# Ordinare il vettore e scegliere la mediana dei valori per minimizzare la distanza

def min_distance(A):
    A.sort()
    leng = len(A)
    min = int((leng/2))
    if leng % 2:                 # caso dispari
        return A[min]
    else:                        # caso pari, ho due possibili indici min e min-1 centrali
        if  A[min] == A[min-1]:
            return A[min]
        mean  = (A[0] + A[leng-1])/2                    # fa la media e poi controlla quale numero ci si avvicina di più tra i due
        if abs(A[min-1] - mean) > abs(A[min] - mean):
            return A[min]
        else:
            return A[min-1]


def input_string():
    nTestCase = input("Inserire il numero di casi di test: ")
    for i in range(int(nTestCase)):
        A = [int(x) for x in input("Inserire vettore dividendo con una virgola: ").split(',')]
        print(A)
        min = min_distance(A)
        print(min)

input_string()

# Complexity O(sort()) sort() = O(n log n)