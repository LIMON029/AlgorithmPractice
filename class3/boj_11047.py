from sys import stdin, stdout

N, K = map(int, stdin.readline().rstrip().split())
coins = []
for _ in range(N):
    coins.append(int(stdin.readline()))
cnt = 0
for i in range(N-1, -1, -1):
    if K < coins[i]:
        continue
    cnt += K // coins[i]
    K %= coins[i]
stdout.write(f"{cnt}\n")
