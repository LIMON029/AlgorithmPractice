from sys import stdin, stdout


def solution():
    for idx in range(1, N + 1):
        for weight in range(1, K + 1):
            if items[idx][0] <= weight:
                dp[idx][weight] = max(items[idx][1] + dp[idx-1][weight-items[idx][0]], dp[idx-1][weight])
            else:
                dp[idx][weight] = dp[idx-1][weight]


N, K = map(int, stdin.readline().rstrip().split())
items = [tuple(0 for _ in range(2))]

for _ in range(N):
    items.append(tuple(map(int, stdin.readline().rstrip().split())))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
solution()
stdout.write(f"{dp[N][K]}")
