"""You have a long car journey ahead of you. You have a cassette recorder, but unfortunately, your best music is on CDs.
 You need to have it on a cassette, so the problem to solve is: you have a cassette that is N minutes long. How do you choose
   the tracks from the CD to get the most out of the cassette space and have the shortest unused space possible?

Assumptions:
- The number of tracks on the CD does not exceed 20.
- No track is longer than N minutes.
- Tracks do not repeat.
- The length of each track is expressed as an integer.
- N is also an integer.

The program should find the set of tracks that best fills the cassette and print it in the same sequence in which the tracks
are stored on the CD.

Input:
Any number of lines. Each contains the value N, (after the space) the number of tracks, and the durations of the tracks.
 For example, from the first line in the sample data: N = 5, the number of tracks = 3, the first track lasts 1 minute, the second 
 3 minutes, the next 4 minutes.

Output:
Set of tracks (and durations) that are the correct solutions and the string 'sum:' and the sum of the duration times.

Sample Input:
5 3 1 3 4
10 4 9 8 4 2
20 4 10 5 7 4
90 8 10 23 1 2 3 4 5 7
45 8 4 10 44 43 12 9 8 2

Sample Output:
1 4 sum:5
8 2 sum:10
10 5 4 sum:19
10 23 1 2 3 4 5 7 sum:55
4 10 12 9 8 2 sum:45"""


def solveCD(tape_size, n, tracks):
    memo = [[0 for _ in range(tape_size+1)] for _ in range(n+1)]
    path = [[0 for _ in range(tape_size+1)] for _ in range(n+1)]
    i = 0
    x = 0

    def dp(i, x):
        if i == n:
            return 0
        
        if memo[i][x] != 0:
            return memo[i][x]
        
        choices = []
        if x + tracks[i] <= tape_size:
            take = dp(i+1, x+tracks[i]) + tracks[i]
            choices.append((take, True))

        skip = dp(i+1, x)
        choices.append((skip, False))
        
        memo[i][x], path[i][x] = max(choices)

        return memo[i][x]

    sum = dp(i, x)

    # Recuperare i brani
    tracks_chosen = []
    while i < n:
        if path[i][x]:
            tracks_chosen.append(tracks[i])
            x += tracks[i]
        i += 1

    return tracks_chosen, sum

while True:
    line = input()

    if line == "":
        break

    tracks = []
    inputs = list(map(int, line.strip().split(" ")))

    tape_size = inputs[0]
    n = inputs[1]
    for i in range(2, len(inputs)):
        tracks.append(inputs[i])

    print(solveCD(tape_size, n, tracks))


