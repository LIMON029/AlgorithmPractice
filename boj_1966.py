from sys import stdin, stdout


def getOrder(printQ, myNum):
    cnt = 1
    while len(printQ) > 1:
        now = printQ.pop(0)
        if max(printQ, key=lambda x: x[1])[1] > now[1]:
            printQ.append(now)
        else:
            if myNum == now[0]:
                return cnt
            cnt += 1
    return cnt


T = int(stdin.readline())

result = []
for i in range(T):
    N, M = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    q = []
    for j in range(N):
        q.append((j, priority[j]))
    result.append(str(getOrder(q, M)))
stdout.write("\n".join(result))
