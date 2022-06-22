from sys import stdin, stdout

N = int(stdin.readline())

DP = [1, 2]
if N >= 3:
    for i in range(2, N):
        DP.append(DP[i-1] + DP[i-2])
    stdout.write(f"{DP[-1] % 10007}")
else:
    stdout.write(f"{N}")
