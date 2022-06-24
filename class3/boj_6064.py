from sys import stdin, stdout

T = int(stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, stdin.readline().rstrip().split())
    calc = x
    isWrong = True
    while calc <= M * N:
        if (calc - x) % M == 0 and (calc - y) % N == 0:
            stdout.write(f"{calc}\n")
            isWrong = False
            break
        calc += M
    if isWrong:
        stdout.write("-1\n")
