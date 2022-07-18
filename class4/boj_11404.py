from sys import stdin, stdout

INF = 1e9


def Floyd():
    global graph, N
    for middle in range(1, N + 1):
        for n_start in range(1, N + 1):
            for n_end in range(1, N + 1):
                if n_start != n_end:
                    graph[n_start][n_end] = min(graph[n_start][n_end], graph[n_start][middle] + graph[middle][n_end])


N = int(stdin.readline())
graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
M = int(stdin.readline())

for _ in range(M):
    a, b, c = map(int, stdin.readline().rstrip().split())
    if graph[a][b] > c:
        graph[a][b] = c

Floyd()
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            stdout.write("0 ")
        else:
            stdout.write(f"{graph[i][j]} ")
    stdout.write("\n")
