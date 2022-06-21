from sys import stdin, stdout
from collections import deque


class Graph:
    def __init__(self, nodeCnt):
        self.nodeCnt = nodeCnt
        self.graph = [[0 for _ in range(nodeCnt + 1)] for _ in range(nodeCnt + 1)]
        self.visited = [0 for _ in range(nodeCnt + 1)]


def BFS():
    global g
    queue = deque()
    cnt = 0
    for node in range(1, g.nodeCnt + 1):
        if g.visited[node] == 1:
            continue
        g.visited[node] = 1
        queue.append(node)
        cnt += 1
        while queue:
            now = queue.popleft()
            for i in range(1, g.nodeCnt + 1):
                if g.graph[now][i] == 1 and g.visited[i] == 0:
                    g.visited[i] = 1
                    queue.append(i)
    stdout.write(f"{cnt}")


N, M = map(int, stdin.readline().rstrip().split())
g = Graph(N)

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    g.graph[a][b], g.graph[b][a] = 1, 1

BFS()
