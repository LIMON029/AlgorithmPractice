from sys import stdin, stdout
from collections import deque


def BFS(p):
    global dx, dy
    global N, M, graph
    queue = deque()
    queue.append(p)

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]

            if x < 0 or x >= M or y < 0 or y >= N:
                continue
            if graph[y][x] == 0:
                continue
            if graph[y][x] == 1:
                graph[y][x] = graph[ny][nx] + 1
                queue.append([x, y])

    stdout.write(f"{graph[N - 1][M - 1]}")


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip())))
BFS([0, 0])
