""" Ecco una descrizione dell'istanza di questo famoso rompicapo che coinvolge N = 2 uova e un edificio con K = 36 piani. 
Supponiamo di voler sapere da quali piani di un edificio di 36 piani è sicuro far cadere le uova e quali faranno rompere 
le uova durante la caduta. Facciamo alcune ipotesi:

1. Un uovo che sopravvive a una caduta può essere riutilizzato.
2. Un uovo rotto deve essere scartato.
3. L'effetto di una caduta è lo stesso per tutte le uova.
4. Se un uovo si rompe quando cade, si romperà anche se caduto da un piano più alto.
5. Se un uovo sopravvive a una caduta, sopravviverà anche a una caduta più breve.
6. Non è escluso che le finestre del primo piano rompano le uova, né è escluso che il 36º piano non faccia rompere un uovo.
Se è disponibile solo un uovo e vogliamo essere sicuri di ottenere il risultato giusto, l'esperimento può essere eseguito in 
un solo modo. Lascia cadere l'uovo dalla finestra del primo piano; se sopravvive, lascialo cadere dalla finestra del secondo piano. 
Continua verso l'alto finché non si rompe. Nel caso peggiore, questo metodo può richiedere 36 cadute. Supponiamo che siano disponibili 
2 uova. Qual è il numero minimo garantito di cadute di uova che funzioneranno in tutti i casi? Il problema non è trovare effettivamente 
il piano critico, ma semplicemente decidere da quali piani far cadere le uova in modo che il numero totale di prove sia ridotto al 
minimo.

Nota: In questo post, discuteremo una soluzione a un problema generale con 'N' uova e 'K' piani. """
import sys
 
MAX = 1000
 
memo = [[-1 for i in range(MAX)] for j in range(MAX)]
 
 
def solveEggDrop(n, k):
 
    if (memo[n][k] != -1):
        return memo[n][k]
 
    if (k == 1 or k == 0):
        return k
 
    if (n == 1):
        return k
 
    min = sys.maxsize
    res = 0
 
    for x in range(1, k+1):
        res = max(solveEggDrop(n - 1, x - 1), solveEggDrop(n, k - x))
        if (res < min):
            min = res
 
    memo[n][k] = min + 1
    return min + 1

print(solveEggDrop(2, 36))

# Time Complexity = O(n*k^2)