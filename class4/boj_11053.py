from sys import stdin, stdout

N = int(stdin.readline())
A = list(map(int, stdin.readline().rstrip().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
stdout.write(f"{max(dp)}")
