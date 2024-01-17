""" Molti problemi nell'informatica implicano il massimizzare una misura in base a dei vincoli.
Considera un esame di storia in cui agli studenti viene chiesto di collocare diversi eventi storici in ordine cronologico. 
Gli studenti che mettono tutti gli eventi nell'ordine corretto riceveranno il massimo dei voti, ma come dovrebbe essere assegnato 
il credito parziale agli studenti che posizionano in modo errato uno o più eventi storici?
Alcune possibilità per il credito parziale includono:
1. 1 punto per ogni evento il cui posizionamento corrisponde al suo posizionamento corretto.
2. 1 punto per ogni evento nella sequenza più lunga (non necessariamente contigua) di eventi che sono nell'ordine corretto rispetto 
gli uni agli altri.
Ad esempio, se quattro eventi sono correttamente ordinati come 1 2 3 4, allora l'ordine 1 3 2 4 otterrebbe un punteggio di 2 utilizzando
il primo metodo (gli eventi 1 e 4 sono posizionati correttamente) e un punteggio di 3 utilizzando il secondo metodo (le sequenze di 
eventi 1 2 4 e 1 3 4 sono entrambe nell'ordine corretto rispetto agli uni agli altri).
In questo problema ti viene chiesto di scrivere un programma per valutare tali domande utilizzando il secondo metodo.
Dati l'ordine cronologico corretto di n eventi 1, 2, ..., n come c1, c2, ..., cn, dove 1 ≤ ci ≤ n indica il posizionamento dell'evento 
i nell'ordine cronologico corretto, e una sequenza di risposte degli studenti r1, r2, ..., rn, dove 1 ≤ ri ≤ n indica il posizionamento 
cronologico dato dall'utente per l'evento i; determinare la lunghezza della sequenza più lunga (non necessariamente contigua) di eventi 
nelle risposte degli studenti che sono nell'ordine cronologico corretto rispetto gli uni agli altri.
Input
Il file di input contiene uno o più casi di test, ognuno descritto come segue.
La prima riga dell'input consisterà in un intero n che indica il numero di eventi con 2 ≤ n ≤ 20. La seconda riga conterrà n interi, 
indicando l'ordine cronologico corretto di n eventi.
Le righe rimanenti consisteranno ciascuna in n interi, con ogni riga che rappresenta l'ordinamento cronologico di un evento da parte 
di uno studente. Tutte le righe conterranno n numeri nell'intervallo [1 . . . n], con ciascun numero che appare esattamente una volta 
per riga e con ogni numero separato dagli altri numeri sulla stessa riga da uno o più spazi.
Output
Per ogni caso di test, l'output deve seguire la descrizione sottostante.
Per ogni posizionamento degli eventi da parte dello studente, il tuo programma dovrebbe stampare il punteggio per quel posizionamento. 
Dovrebbe esserci una riga di output per ogni posizionamento dello studente.
Avviso: Leggi attentamente la descrizione e considera la differenza tra 'ordering' e 'ranking'. """


def solveLCS(s1, s2):
    n = len(s1)
    m = len(s2)
    memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
    i, j = 0, 0

    def LCS(i, j):

        if i == n or j == m:
            return 0

        if memo[i][j] != 0:
            return memo[i][j]
        
        equal = 0
        if s1[i] == s2[j]   :
            equal = LCS(i+1, j+1) + 1

        memo[i][j] = max(equal, LCS(i+1, j), LCS(i, j+1))

        return memo[i][j]
    
    return LCS(i, j)


print(solveLCS([3, 1, 2, 4, 9, 5, 10, 6, 8, 7], [2, 10, 1, 3, 8, 4, 9, 5, 7, 6]))