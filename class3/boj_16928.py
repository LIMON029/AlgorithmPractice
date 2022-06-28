from sys import stdin, stdout
from collections import deque


def BFS():
    global ladder, snake
    ladders, snakes = ladder.keys(), snake.keys()
    visited = [False for _ in range(101)]
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        now = queue.popleft()
        for d in range(1, 7):
            next_point = now + d
            if 0 <= next_point < 101 and not visited[next_point]:
                if next_point in ladders:
                    next_point = ladder[next_point]

                if next_point in snakes:
                    next_point = snake[next_point]

                if not visited[next_point]:
                    queue.append(next_point)
                    visited[next_point] = True
                    board[next_point] = board[now] + 1


N, M = map(int, stdin.readline().rstrip().split())
board = [0 for i in range(101)]

ladder = {}
snake = {}
for _ in range(N):
    x, y = map(int, stdin.readline().rstrip().split())
    ladder[x] = y
for _ in range(M):
    x, y = map(int, stdin.readline().rstrip().split())
    snake[x] = y

BFS()
stdout.write(f"{board[100]}")
