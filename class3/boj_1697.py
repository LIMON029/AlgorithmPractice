from sys import stdin, stdout
from collections import deque


def BFS():
    global N, K
    q = deque([N])
    visited = [0 for _ in range(100001)]

    while q:
        now = q.popleft()
        if now == K:
            return visited[now]
        for nextNum in (now - 1, now + 1, 2 * now):
            if 0 <= nextNum <= 100000 and visited[nextNum] == 0:
                visited[nextNum] = visited[now] + 1
                q.append(nextNum)


N, K = map(int, stdin.readline().split())
stdout.write(f"{BFS()}")
