from sys import stdin, stdout

T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    dp = [[] for _ in range(2)]
    for i in range(2):
        dp[i] = list(map(int, stdin.readline().rstrip().split()))
    if n == 1:
        stdout.write(f"{max(dp[0][n-1], dp[1][n-1])}\n")
        continue
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j-2], dp[1][j-1])
        dp[1][j] += max(dp[0][j-2], dp[0][j-1])
    stdout.write(f"{max(dp[0][n-1], dp[1][n-1])}\n")
