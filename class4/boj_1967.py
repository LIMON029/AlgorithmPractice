from sys import stdin, stdout


def DFS(distance, now, w):
    global graph, n
    stack = [[now, w]]
    while stack:
        node, weight = stack.pop()
        for n_node, n_weight in graph[node]:
            if distance[n_node][1] == -1:
                distance[n_node][1] = n_weight + weight
                stack.append([n_node, n_weight + weight])


n = int(stdin.readline())

graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    p, c, w = map(int, stdin.readline().rstrip().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

dist = [[i, -1] for i in range(n + 1)]
dist[1][1] = 0
DFS(dist, 1, 0)

new_start = max(dist, key=lambda x: x[1])[0]
dist = [[i, -1] for i in range(n + 1)]
dist[new_start][1] = 0
DFS(dist, new_start, 0)

stdout.write(f"{max(dist, key=lambda x: x[1])[1]}\n")
