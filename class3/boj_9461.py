from sys import stdin, stdout

T = int(stdin.readline())
DP = [1, 1, 1, 2, 2] # 3 4
for _ in range(T):
    N = int(stdin.readline())
    if N < 6:
        stdout.write(f"{DP[N-1]}\n")
    else:
        now = len(DP)
        if now < N - 1:
            for i in range(now, N):
                DP.append(DP[i-1] + DP[i-5])
        stdout.write(f"{DP[N-2] + DP[N-6]}\n")
