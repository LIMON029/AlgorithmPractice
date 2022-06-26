from sys import stdin, stdout

n = int(stdin.readline())
dp = [1, 1]
for i in range(2, n+1):
    dp.append(dp[i-1] + (dp[i-2] * 2))
stdout.write(f"{dp[n] % 10007}")
