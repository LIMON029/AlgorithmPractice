from sys import stdin, stdout

n = int(stdin.readline())
stack = []
result = []
isDone = True
now = 1
for i in range(n):
    num = int(stdin.readline())
    while now <= num:
        stack.append(now)
        result.append("+")
        now += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        isDone = False
        break

stdout.write("\n".join(result) if isDone else "NO\n")
