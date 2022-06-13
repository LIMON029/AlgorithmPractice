from sys import stdin, stdout
from collections import deque


class Graph:
    def __init__(self, nodeCnt):
        self.graph = [[0 for _ in range(nodeCnt)] for _ in range(nodeCnt)]
        self.nodeCnt = nodeCnt


def BFS(g, node):
    queue = deque()
    visited = [0 for _ in range(g.nodeCnt)]
    visited[node] = 1
    distance = [0 for _ in range(g.nodeCnt)]

    queue.append(node)

    while queue:
        now = queue.popleft()
        for i in range(g.nodeCnt):
            if g.graph[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                distance[i] = distance[now] + 1
    return sum(distance)


N, M = map(int, stdin.readline().split())
G = Graph(N+1)
for _ in range(M):
    x, y = map(int, stdin.readline().split())
    G.graph[x][y], G.graph[y][x] = 1, 1

result = []
for n in range(1, N + 1):
    result.append(BFS(G, n))

stdout.write(f"{result.index(min(result))+1}\n")
