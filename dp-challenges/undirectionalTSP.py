""" I problemi che richiedono percorsi minimi attraverso un certo dominio appaiono in molte aree diverse dell'informatica. 
Ad esempio, uno dei vincoli nei problemi di routing VLSI è la minimizzazione della lunghezza del filo. 
Il Problema del Commesso Viaggiatore (TSP) - trovare se tutte le città nel percorso di un commesso viaggiatore possono essere 
visitate esattamente una volta con un limite specificato di tempo di viaggio - è uno degli esempi canonici di un problema NP-completo;
le soluzioni sembrano richiedere un tempo eccessivo per essere generate, ma sono semplici da verificare.

Questo problema riguarda la ricerca di un percorso minimo attraverso una griglia di punti viaggiando solo da sinistra a destra.

Dato una matrice m×n di numeri interi, devi scrivere un programma che calcoli un percorso di peso minimo. Un percorso inizia da 
qualsiasi punto nella colonna 1 (la prima colonna) e consiste in una sequenza di passi che terminano nella colonna n (l'ultima colonna). Un passo consiste nel viaggiare dalla colonna i alla colonna i + 1 in una riga adiacente (orizzontale o diagonale). Le prime e ultime righe (righe 1 e m) di una matrice sono considerate adiacenti, ovvero la matrice "avvolge" in modo che rappresenti un cilindro orizzontale. I passi legali sono illustrati a destra.

Il peso di un percorso è la somma dei numeri interi in ciascuna delle n celle della matrice che vengono visitate. Ad esempio, 
sono mostrate due matrici leggermente diverse di dimensioni 5×6 di seguito (l'unica differenza sono i numeri nell'ultima riga). 
Il percorso minimo è illustrato per ciascuna matrice. Nota che il percorso per la matrice a destra sfrutta la proprietà di adiacenza 
delle prime e ultime righe.

**Input:**
L'input consiste in una sequenza di specifiche di matrici. Ogni specifica di matrice consiste nelle dimensioni delle righe 
e delle colonne in quell'ordine su una riga seguita da m · n numeri, dove m è la dimensione delle righe e n è la dimensione 
delle colonne. Gli interi appaiono in input in ordine di riga principale, cioè i primi n interi costituiscono la prima riga 
della matrice, i secondi n interi costituiscono la seconda riga e così via. Gli interi su una riga saranno separati da uno o 
più spazi. Nota: gli interi non sono limitati a essere positivi.

Ci saranno una o più specifiche di matrici in un file di input. L'input è terminato da fine-file. Per ogni specifica, il numero
 di righe sarà compreso tra 1 e 10 inclusi; il numero di colonne sarà compreso tra 1 e 100 inclusi. Il peso del percorso non supererà 
 i valori interi rappresentabili utilizzando 30 bit.

**Output:**
Dovrebbero essere stampate due righe per ogni specifica di matrice nel file di input, la prima riga rappresenta un 
percorso di peso minimo, e la seconda riga è il costo di un percorso minimo. Il percorso consiste in una sequenza di n numeri 
(separati da uno o più spazi) che rappresentano le righe che costituiscono il percorso minimo. Se ci sono più di un percorso di 
peso minimo, dovrebbe essere stampato il percorso che è lessicograficamente più piccolo.

Nota: Lessicograficamente significa l'ordine naturale sulle sequenze indotto dall'ordine dei loro elementi. """

def solveUnidirectionalTSP(n, m, matrix):
    memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    def uTSP(i, j):
        if j == m:
            return 0

        if i == n:
            i = 0
        if i == -1:
            i = n-1

        if memo[i][j] != -1:
            return memo[i][j]
        
        memo[i][j] = min(uTSP(i-1, j+1) + matrix[i][j],
                         uTSP(i, j+1) + matrix[i][j],
                         uTSP(i+1,j+1) + matrix[i][j])
        
        return memo[i][j]
    min_list = []
    for i in range(n):
        min_list.append(uTSP(i, 0))
    
    return min(min_list)

dims = input("inserire rows e cols: ")

n, m = map(int, dims.strip().split(" "))

matrix = []
for i in range(n):
    linea = input("inserire riga " + str(i+1) + ":")

    matrix.append(list(map(int, linea.strip().split(" "))))

print(solveUnidirectionalTSP(n, m, matrix))


    
    