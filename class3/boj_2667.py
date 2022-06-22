from sys import stdin, stdout
from collections import deque


def BFS(maxCol, start_x, start_y):
    global dx, dy, graph
    queue = deque()
    queue.append((start_x, start_y))
    graph[start_y][start_x] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < maxCol and 0 <= ny < maxCol:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(stdin.readline())
graph = []
allCnt = []

for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            allCnt.append(BFS(N, j, i))

stdout.write(f"{len(allCnt)}\n")
stdout.write("\n".join(map(str, sorted(allCnt))))
