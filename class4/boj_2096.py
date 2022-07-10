from sys import stdin, stdout

N = int(stdin.readline())

a, b, c = map(int, stdin.readline().rstrip().split())
max_dp = [a, b, c]
min_dp = [a, b, c]
for _ in range(N-1):
    a, b, c = map(int, stdin.readline().rstrip().split())
    max_tmp = [0 for _ in range(3)]
    min_tmp = [0 for _ in range(3)]
    for i in range(3):
        if i == 0:
            max_tmp[i] = a + max(max_dp[i], max_dp[i+1])
            min_tmp[i] = a + min(min_dp[i], min_dp[i+1])
        elif i == 1:
            max_tmp[i] = b + max(max_dp[i-1], max_dp[i], max_dp[i+1])
            min_tmp[i] = b + min(min_dp[i-1], min_dp[i], min_dp[i+1])
        else:
            max_tmp[i] = c + max(max_dp[i], max_dp[i-1])
            min_tmp[i] = c + min(min_dp[i], min_dp[i-1])
    max_dp = max_tmp.copy()
    min_dp = min_tmp.copy()

stdout.write(f"{max(max_dp)} {min(min_dp)}")
