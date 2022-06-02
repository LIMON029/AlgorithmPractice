class Graph:
    def __init__(self, maxCol):
        self.maxCol = maxCol
        self.graph = [
            [1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0]
        ]
        self.visited = [[0 for _ in range(self.maxCol)] for _ in range(self.maxCol)]


def DFS(g, x, y, endx, endy):
    global dx, dy
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < g.maxCol and 0 <= ny < g.maxCol:
                if g.graph[ny][nx] == 1 and g.visited[ny][nx] == 0:
                    stack.append((nx, ny))
                    g.visited[ny][nx] = g.visited[y][x] + 1
                    if nx == g.maxCol - 1 and ny == g.maxCol - 1:
                        break
    return g.visited[endy][endx]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

maxCol = 7
maze = Graph(maxCol)
n = DFS(maze, 0, 0, 5, 6)
for i in range(maxCol):
    print(maze.visited[i])
print(n)
