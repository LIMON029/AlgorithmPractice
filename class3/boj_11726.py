from sys import stdin, stdout


def getResult(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return getResult(n-1) + getResult(n - 2)


N = int(stdin.readline())


stdout.write(f"{getResult(N) % 10007}")
