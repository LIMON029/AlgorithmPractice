from sys import stdin, stdout

K = int(stdin.readline())
stack = []
for i in range(K):
    num = int(stdin.readline())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)
stdout.write(f"{sum(stack)}")
