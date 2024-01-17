"""
Given an even number (greater than 2 ), print two prime numbers whose sum will be equal to given number. 
There may be several combinations possible. Print only first such pair. 
"""

MAX_PRIME = 1000

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
        
def findPrimes(sum):
    primes = []

    for i in range(2, sum+1):
        if isPrime(i):
            primes.append(i)

    return primes


def backtrack(pair, sum, primes, l):

    if l == 2:
        if pair[0] + pair[1] == sum:
            print(pair[0], pair[1])
            return True
        return False
    
    for i in primes:
        pair[l] = i
        if backtrack(pair, sum, primes, l+1):
            return True

    return False

def solvePrimeSum(sum):
    pair = [None]*2
    primes = findPrimes(sum)

    if backtrack(pair, sum, primes, 0):
        pass
    else:
        print("soluzione inesistente")


def process_input():

    with open("sum.txt", 'r') as file:

        nCase = int(file.readline().strip())

        for i in range(nCase):
            sum = int(file.readline())
            print(sum)

            solvePrimeSum(sum)

process_input()