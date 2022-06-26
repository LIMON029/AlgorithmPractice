from sys import stdin, stdout


def tetromino(i, j):
    global paper, types, N, M, max_sum
    for case in types.values():
        now = 0
        for d in range(4):
            nx = j + case[d][0]
            ny = i + case[d][1]
            if 0 <= nx < M and 0 <= ny < N:
                now += paper[ny][nx]
        max_sum = max(max_sum, now)


types = {
    11: [(0, 0), (1, 0), (2, 0), (3, 0)],       # │
    12: [(0, 0), (0, 1), (0, 2), (0, 3)],       # ─
    21: [(0, 0), (1, 0), (0, 1), (1, 1)],       # □
    31: [(0, 0), (0, 1), (0, 2), (1, 2)],       # └
    32: [(0, 0), (1, 0), (2, 0), (0, 1)],       # ┌──
    33: [(0, 0), (1, 0), (1, 1), (1, 2)],       # ┐
    34: [(0, 0), (1, 0), (2, 0), (2, -1)],      # ──┘
    35: [(0, 0), (1, 0), (1, -1), (1, -2)],     # ┘
    36: [(0, 0), (1, 0), (2, 0), (0, -1)],     # └──
    37: [(0, 0), (0, 1), (0, 2), (1, 0)],       # ┌
    38: [(0, 0), (1, 0), (2, 0), (2, 1)],       # ──┐
    41: [(0, 0), (0, 1), (1, 1), (1, 2)],
    42: [(0, 0), (1, 0), (1, -1), (2, -1)],
    43: [(0, 0), (0, 1), (1, 0), (1, -1)],
    44: [(0, 0), (1, 0), (1, 1), (2, 1)],
    51: [(0, 0), (1, 0), (2, 0), (1, 1)],
    52: [(0, 0), (1, 0), (1, -1), (1, 1)],
    53: [(0, 0), (1, 0), (2, 0), (1, -1)],
    54: [(0, 0), (0, 1), (0, 2), (1, 1)]
}

N, M = map(int, stdin.readline().rstrip().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, stdin.readline().rstrip().split())))

max_sum = 0

for i in range(N):
    for j in range(M):
        tetromino(i, j)

stdout.write(f"{max_sum}")
