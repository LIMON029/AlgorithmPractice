from sys import stdin, stdout
from collections import deque


def BFS(x, y, visited):
    global matrix, dx, dy, N
    queue = deque()
    queue.append((x, y))
    visited[y][x] = 1
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                a = matrix[ny][nx]
                b = matrix[y][x]
                if matrix[ny][nx] == matrix[y][x] and visited[ny][nx] == 0:
                    queue.append((nx, ny))
                    visited[ny][nx] = 1


def getCnt():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    n_cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(j, i, visited)
                n_cnt += 1
    stdout.write(f"{n_cnt} ")


N = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = []
for _ in range(N):
    matrix.append(list(map(str, stdin.readline().rstrip())))

getCnt()

for i in range(N):
    for j in range(N):
        if matrix[j][i] == 'R':
            matrix[j][i] = 'G'
getCnt()
