from sys import stdin, stdout


def getResult():
    global matrix, N, M, B
    totalTime = float('inf')
    result = 0
    for height in range(257):
        up, down = 0, 0
        for y in range(N):
            for x in range(M):
                if matrix[y][x] >= height:
                    down += matrix[y][x] - height
                else:
                    up += height - matrix[y][x]
        if up <= down + B and totalTime >= (up + down * 2):
            totalTime = up + down * 2
            result = height
    return f"{totalTime} {result}"


N, M, B = map(int, stdin.readline().split())
matrix = tuple(tuple(map(int, stdin.readline().split())) for _ in range(N))
stdout.write(getResult())
