from sys import stdin, stdout


def getCnt(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4
    return getCnt(num-1) + getCnt(num-2) + getCnt(num-3)


T = int(stdin.readline())

result = []
for i in range(T):
    n = int(stdin.readline())
    result.append(str(getCnt(n)))
stdout.write("\n".join(result))
