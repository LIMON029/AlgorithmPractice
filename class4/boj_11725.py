from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10**5)

N = int(stdin.readline())
graph = [[] for _ in range(N+1)]
root = [0 for _ in range(N+1)]
for _ in range(N - 1):
    a, b = map(int, stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(node):
    for now in graph[node]:
        if root[now] == 0:
            root[now] = node
            DFS(now)


DFS(1)

for n in range(2, N + 1):
    stdout.write(f"{root[n]}\n")
