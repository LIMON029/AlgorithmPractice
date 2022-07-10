from sys import stdin, stdout
from collections import deque


def BFS():
    global graph, N, M
    global dx, dy
    queue = deque()
    queue.append([0, 0, 0])
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while queue:
        x, y, broken = queue.popleft()

        if x == M - 1 and y == N - 1:
            return visited[y][x][broken]

        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and broken == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    queue.append([nx, ny, 1])
                elif graph[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                    visited[ny][nx][broken] = visited[y][x][broken] + 1
                    queue.append([nx, ny, broken])
    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, stdin.readline().rstrip().split())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, list(stdin.readline().rstrip())))

stdout.write(f"{BFS()}")
