from sys import stdin, stdout


def get_paper_cnt(nx, ny, win_size):
    global matrix, zero, one

    now = matrix[ny][nx]
    for i in range(ny, ny + win_size):
        for j in range(nx, nx + win_size):
            if matrix[i][j] != now:
                new_size = win_size // 2
                get_paper_cnt(nx, ny, new_size)
                get_paper_cnt(nx + new_size, ny, new_size)
                get_paper_cnt(nx, ny + new_size, new_size)
                get_paper_cnt(nx + new_size, ny + new_size, new_size)
                return

    if now == 0:
        zero += 1
    else:
        one += 1


N = int(stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, stdin.readline().split())))
zero, one = 0, 0
get_paper_cnt(0, 0, N)
stdout.write(f"{zero}\n{one}")
