from sys import stdin, stdout

# M : 가로 길이, N: 세로 길이, K: 배추 개수


def BFS(matrix, x, y):
    global M, N
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    queue = [(x, y)]
    matrix[y][x] = 0
    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if matrix[ny][nx] == 1:
                matrix[ny][nx] = 0
                queue.append((nx, ny))
    return


def getResult(matrix):
    global M, N
    count = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                BFS(matrix, x, y)
                count += 1
    return count


T = int(stdin.readline())
resultList = []
for i in range(T):
    M, N, K = map(int, stdin.readline().split())
    farm = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(K):
        X, Y = map(int, stdin.readline().split())
        farm[Y][X] = 1
    resultList.append(str(getResult(farm)))
stdout.write("\n".join(resultList))
