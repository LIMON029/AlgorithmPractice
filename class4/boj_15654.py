from sys import stdin, stdout


def solve(now):
    if now == M:
        stdout.write(" ".join(map(str, result)) + "\n")
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(nums[i])
            solve(now + 1)
            result.pop()
            visited[i] = False


N, M = map(int, stdin.readline().rstrip().split())
nums = sorted(list(map(int, stdin.readline().rstrip().split())))
visited = [False for _ in range(N)]
result = []
solve(0)
