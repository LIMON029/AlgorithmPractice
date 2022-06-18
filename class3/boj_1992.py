from sys import stdin, stdout


def divAndCheck(x, y, n):
    global matrix, result
    now = matrix[y][x]

    for i in range(y, y + n):
        for j in range(x, x + n):
            if now != matrix[i][j]:
                result.append("(")
                next_size = n // 2
                divAndCheck(x, y, next_size)
                divAndCheck(x + next_size, y, next_size)
                divAndCheck(x, y + next_size, next_size)
                divAndCheck(x + next_size, y + next_size, next_size)
                result.append(")")
                return
    result.append(now)


N = int(stdin.readline())
matrix = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]
result = []
divAndCheck(0, 0, N)
stdout.write("".join(map(str, result)))
