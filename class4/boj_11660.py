from sys import stdin, stdout

N, M = map(int, stdin.readline().rstrip().split())
matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    matrix[i][1:N+1] = list(map(int, stdin.readline().rstrip().split()))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        matrix[i][j] = matrix[i][j] + matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
    stdout.write(f"{matrix[x2][y2] - matrix[x2][y1-1] - matrix[x1-1][y2] + matrix[x1-1][y1-1]}\n")
