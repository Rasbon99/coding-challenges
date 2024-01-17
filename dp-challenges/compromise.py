""" In a few months the European Currency Union will become a reality. However, to join the club, the
Maastricht criteria must be fulfilled, and this is not a trivial task for the countries (maybe except for
Luxembourg). To enforce that Germany will fulfill the criteria, our government has so many wonderful
options (raise taxes, sell stocks, revalue the gold reserves,...) that it is really hard to choose what to
do.
Therefore the German government requires a program for the following task:
Two politicians each enter their proposal of what to do. The computer then outputs the
longest common subsequence of words that occurs in both proposals. As you can see, this
is a totally fair compromise (after all, a common sequence of words is something what both
people have in mind).
Your country needs this program, so your job is to write it for us.
Input
The input file will contain several test cases.
Each test case consists of two texts. Each text is given as a sequence of lower-case words, separated
by whitespace, but with no punctuation. Words will be less than 30 characters long. Both texts will
contain less than 100 words and there will be at least one common word in each text. Each text will
be terminated by a line containing a single ‘#’.
Input is terminated by end of file.
Output
For each test case, print the longest common subsequence of words occuring in the two texts. If there
is more than one such sequence, any one is acceptable. Separate the words by one blank. After the last
word, output a newline character.
Sample Input
die einkommen der landwirte
sind fuer die abgeordneten ein buch mit sieben siegeln
um dem abzuhelfen
muessen dringend alle subventionsgesetze verbessert werden
#
die steuern auf vermoegen und einkommen
sollten nach meinung der abgeordneten
nachdruecklich erhoben werden
dazu muessen die kontrollbefugnisse der finanzbehoerden
dringend verbessert werden
#
Sample Output
die einkommen der abgeordneten muessen dringend verbessert werden """

def solveCompromise(sentence1, sentence2):
    n = len(sentence1)
    m = len(sentence2)
    memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    path = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    i, j = 0, 0

    def dp(i, j):
        if i == n or j == m:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        take = (0, False)
        if sentence1[i] == sentence2[j]:
            take = (dp(i+1, j+1) + 1, True)

        not_take1 = (dp(i+1, j), False)
        not_take2 = (dp(i, j+1), False)

        memo[i][j], path[i][j] = max(take, not_take1, not_take2)

        return memo[i][j]
    
    dp(i, j)
    
    result = []
    i, j = 0, 0
    while i < n and j < m:
        if path[i][j]:
            result.append(sentence1[i])
            i += 1
            j += 1
        elif memo[i+1][j] > memo[i][j+1]:
            i += 1
        else:
            j += 1
          
    result = " ".join(result)

    return result

lista1 = [
    "die", "einkommen", "der", "landwirte",
    "sind", "fuer", "die", "abgeordneten", "ein", "buch", "mit", "sieben", "siegeln",
    "um", "dem", "abzuhelfen",
    "muessen", "dringend", "alle", "subventionsgesetze", "verbessert", "werden"
]

lista2 = [
    "die", "steuern", "auf", "vermoegen", "und", "einkommen",
    "sollten", "nach", "meinung", "der", "abgeordneten",
    "nachdruecklich", "erhoben", "werden",
    "dazu", "muessen", "die", "kontrollbefugnisse", "der", "finanzbehoerden",
    "dringend", "verbessert", "werden"
]


print(solveCompromise(lista1, lista2))




        