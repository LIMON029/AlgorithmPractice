from sys import stdin, stdout

N = int(stdin.readline())

costs = []

for _ in range(N):
    costs.append(list(map(int, stdin.readline().rstrip().split())))

for i in range(1, N):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

stdout.write(f"{min(costs[N-1])}")
