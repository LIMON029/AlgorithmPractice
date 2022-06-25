from sys import stdin, stdout


def FW():
    global matrix, N
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matrix[j][k] = 1 if matrix[j][k] | (matrix[j][i] + matrix[i][k] == 2) else 0


N = int(stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, stdin.readline().rstrip().split())))
FW()
for line in matrix:
    stdout.write(" ".join(map(str, line))+"\n")
