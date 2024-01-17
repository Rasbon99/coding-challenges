"""
To create a program that takes input value 'n' and prints all possible permutations.
"""

def generate_permutations(n):
    a = [None]*n               # uso set per essere sicuro di non avere duplicati
    backtrack(a, 0, n)


def backtrack(a, k, n):
    c = list()
    nc = n

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
    print(a)

def construct_candidates(a, k, n, c, nc):
    if n == 0:                              # Se n è zero, non ci sono candidati da generare, quindi restituisci una lista vuota
        return [], 0            
    c = list((range(1, n + 1)))             # Inizializziamo la lista dei candidati come una sequenza da 1 a n
    if a is not None:
        for i in range(k-1):                # Se a non è None, rimuoviamo gli elementi già presenti in a dalla lista dei candidati
            if a[i] in c:
                c.remove(a[i])
    nc = len(c)
    return c, nc

generate_permutations(3)

# Complexity O(n!)