"""
To write a program that, given the input value of elements 'n', outputs all possible subsets
"""

"""
Solution
To construct all 2**n subsets, set up an array/vector of n cells, where the value of ai is either true or false, 
signifying whether the ith item is or is not in the subset. 
To use the notation of the general backtrack algorithm, Sk = (true, false), and v is a solution whenever k major equal n.
"""

def generate_subsets(n):
    a = [None]*n      
    backtrack(a, 0, n)


def backtrack(a, k, n):
    c = [None]*2
    nc = 0

    if is_a_solution(a, k, n):
        process_solution(a, k, n)
    else:
        k = k + 1           # prossimo livello
        c, nc = construct_candidates(a, k, n, c, nc)
        for i in range(nc):
            a[k - 1] = c[i]
            backtrack(a, k, n)


def is_a_solution(a, k, n):
    return (k == n)         # torna vero solo se ho questa condizione


def process_solution(a, k, n):
    subset = []
    for i in range(k):
        if a[i]:
            subset.append(i + 1)
    print(subset)

def construct_candidates(a, k, n, c, nc):
    # Inizializziamo una lista di candidati per il livello da esplorare.
    # Per il caso dei sottoinsiemi, possiamo avanzare utilizzando un valore
    # True (indicante l'indice dell'albero da mettere nel sottoinsieme finale)
    # o False (indicante il valore che non deve essere incluso nel sottoinsieme).
    c = [True, False]
    nc = 2
    return c, nc

generate_subsets(3)

# Complexiy O(2^n)