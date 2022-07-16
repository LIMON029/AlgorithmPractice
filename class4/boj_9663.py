from sys import stdin, stdout


def keepGoing(now):
    global result
    for i in range(now):
        if result[now] == result[i] or now - i == abs(result[now] - result[i]):
            return False
    return True


def findNQueen(now):
    global result, N, ans
    if now == N:
        ans += 1
        return

    for i in range(N):
        result[now] = i
        if keepGoing(now):
            findNQueen(now + 1)


N = int(stdin.readline())

result = [0 for _ in range(N)]
ans = 0
findNQueen(0)
stdout.write(f"{ans}")
