from sys import stdin, stdout
from collections import deque

# n = ((d1 * 10 + d2) * 10 + d3) * 10 + d4
# D: n을 두배로 (단, 9999보다 크면 mod 10000 저장)
# S: n-1 (n=0이면 9999저장)
# L: 각 자릿수 왼쪽으로 회전
# R: 각 자릿수 오른쪽으로 회전


def processor(num, case):
    if case == 'D':
        return (num * 2) % 10000
    elif case == 'S':
        return (num - 1) % 10000
    elif case == 'L':
        start = num // 1000
        return (num % 1000) * 10 + start
    elif case == 'R':
        end = num % 10
        return (num // 10) + (end * 1000)


def BFS():
    global A, B, process_type
    visited = [0 for _ in range(10000)]

    queue = deque()
    queue.append((A, ""))
    visited[A] = 1

    while queue:
        n_num, process = queue.popleft()
        if n_num == B:
            stdout.write(f"{process}\n")
            break
        for i in range(4):
            result = processor(n_num, process_type[i])
            if visited[result] == 0:
                queue.append((result, process + process_type[i]))
                visited[result] = 1


process_type = ['D', 'S', 'L', 'R']

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int, stdin.readline().rstrip().split())
    BFS()
