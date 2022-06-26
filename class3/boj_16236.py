from sys import stdin, stdout
from collections import deque


class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2


def getShark():
    global matrix
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                return Shark(j, i)


def BFS():
    global matrix, dx, dy, N, shark
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((shark.x, shark.y))
    visited[shark.y][shark.x] = 1
    result = []
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if matrix[ny][nx] <= shark.size:
                    queue.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
                    if matrix[ny][nx] != 0 and matrix[ny][nx] < shark.size:
                        result.append((nx, ny, visited[ny][nx]-1))
    return sorted(result, key=lambda a: (-a[2], -a[1], -a[0]))


N = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, stdin.readline().rstrip().split())))

shark = getShark()

time = 0
cnt = 0
while True:
    eaten_fishes = BFS()
    if not eaten_fishes:
        break

    now_x, now_y, distance = eaten_fishes.pop()
    time += distance
    matrix[shark.y][shark.x], matrix[now_y][now_x] = 0, 0
    shark.x = now_x
    shark.y = now_y

    cnt += 1

    if cnt == shark.size:
        shark.size += 1
        cnt = 0

stdout.write(f"{time}")
