N, M = map(int, input().split())
board = []
repair = []
for i in range(N):
    board.append(list(input()))

for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for a in range(i, i + 8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if board[a][b] != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1

        repair += [w_cnt, b_cnt]
print(min(repair))
