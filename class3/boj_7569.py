from sys import stdin, stdout
from collections import deque


def BFS():
    global graph, queue, M, N, H
    global dx, dy, dz
    while queue:
        x, y, z = queue.popleft()
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if graph[nz][ny][nx] == 0:
                    queue.append((nx, ny, nz))
                    graph[nz][ny][nx] = graph[z][y][x] + 1


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, stdin.readline().rstrip().split())
graph = []
queue = deque()
for f in range(H):
    floor = []
    for i in range(N):
        floor.append(list(map(int, stdin.readline().rstrip().split())))
        for j in range(M):
            if floor[i][j] == 1:
                queue.append((j, i, f))
    graph.append(floor)

BFS()

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                stdout.write("-1")
                exit(0)
        day = max(day, max(j))
stdout.write(f"{day-1}")
