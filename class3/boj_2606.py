from sys import stdin, stdout
from collections import deque


class Graph:
    def __init__(self, nodeCnt):
        self.graph = [[0 for _ in range(nodeCnt)] for _ in range(nodeCnt)]
        self.visited = [0 for _ in range(nodeCnt)]
        self.nodeCnt = nodeCnt


def BFS(start):
    global g
    queue = deque()
    g.visited[start] = 1
    cnt = 0
    queue.append(start)

    while queue:
        now = queue.popleft()
        for i in range(g.nodeCnt):
            if g.graph[now][i] == 1 and g.visited[i] == 0:
                g.visited[i] = 1
                queue.append(i)
                cnt += 1

    return cnt


N = int(stdin.readline())
M = int(stdin.readline())
g = Graph(N)
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    g.graph[a-1][b-1], g.graph[b-1][a-1] = 1, 1
stdout.write(f"{BFS(0)}")
