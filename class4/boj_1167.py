from sys import stdin, stdout


def DFS(node, dist):
    global tree, visited
    for n, d in tree[node]:
        if visited[n] == 0:
            visited[n] = dist + d
            DFS(n, dist + d)


V = int(stdin.readline())

tree = [[] for _ in range(V + 1)]
for _ in range(V):
    inputs = tuple(map(int, stdin.readline().rstrip().split()[:-1]))
    for i in range(1, len(inputs)-1, 2):
        tree[inputs[0]].append((inputs[i], inputs[i+1]))

visited = [0 for _ in range(V+1)]
visited[1] = 1
DFS(1, 0)

far_from_1 = visited.index(max(visited))
visited = [0 for _ in range(V+1)]
visited[far_from_1] = 1
DFS(far_from_1, 0)

stdout.write(f"{max(visited)}")
