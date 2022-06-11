from sys import stdin, stdout


class Graph:
    def __init__(self, nodeCnt):
        self.nodeCnt = nodeCnt
        self.graph = [[0 for _ in range(nodeCnt)] for _ in range(nodeCnt)]
        self.dfs_visited = [0 for _ in range(nodeCnt)]
        self.bfs_visited = [0 for _ in range(nodeCnt)]


def DFS(g, node):
    global dfs_result
    dfs_result.append(str(node + 1))
    g.dfs_visited[node] = 1
    for i in range(g.nodeCnt):
        if g.graph[node][i] == 1 and g.dfs_visited[i] == 0:
            DFS(g, i)


def BFS(g, node):
    global bfs_result
    bfs_result.append(str(node + 1))
    g.bfs_visited[node] = 1

    queue = [node]

    while queue:
        now = queue.pop(0)
        for i in range(g.nodeCnt):
            if g.graph[now][i] == 1 and g.bfs_visited[i] == 0:
                bfs_result.append(str(i + 1))
                g.bfs_visited[i] = 1
                queue.append(i)


dfs_result = []
bfs_result = []

N, M, V = map(int, stdin.readline().split())
graph = Graph(N)
for i in range(M):
    n1, n2 = map(int, stdin.readline().split())
    graph.graph[n1-1][n2-1], graph.graph[n2-1][n1-1] = 1, 1
DFS(graph, V-1)
BFS(graph, V-1)
stdout.write(" ".join(dfs_result) + "\n")
stdout.write(" ".join(bfs_result))
