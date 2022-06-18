from sys import stdin, stdout

N = int(stdin.readline())
stairs = [0 for _ in range(300)]
for i in range(N):
    stairs[i] = int(stdin.readline())
score = [0 for _ in range(300)]
score[0], score[1] = stairs[0], stairs[0] + stairs[1]
score[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
for j in range(3, N):
    score[j] = stairs[j] + max(score[j-3] + stairs[j-1], score[j-2])
stdout.write(f"{score[N-1]}")
