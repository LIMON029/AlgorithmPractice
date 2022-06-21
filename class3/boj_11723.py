from sys import stdin, stdout

M = int(stdin.readline())
S = set()
for _ in range(M):
    calc = stdin.readline().rstrip().split()
    if calc[0] == "all":
        S = set(str(i) for i in range(1, 21))
        continue
    if calc[0] == "empty":
        S.clear()
        continue
    if calc[1] in S:
        if calc[0] == "remove":
            S.remove(calc[1])
        elif calc[0] == "toggle":
            S.remove(calc[1])
        elif calc[0] == "check":
            stdout.write("1\n")
    else:
        if calc[0] == "add":
            S.add(calc[1])
        elif calc[0] == "check":
            stdout.write("0\n")
        elif calc[0] == "toggle":
            S.add(calc[1])
