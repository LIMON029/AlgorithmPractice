import math
from sys import stdin, stdout

N = int(stdin.readline())
dp = [0, 1]

if N == int(math.sqrt(N))**2:
    stdout.write("1")
    exit(0)

for n in range(2, N+1):
    now = 1e10
    j = 1
    while (j ** 2) <= n:
        now = min(now, dp[n - (j**2)])
        j += 1
    dp.append(now + 1)

stdout.write(f"{dp[N]}")
