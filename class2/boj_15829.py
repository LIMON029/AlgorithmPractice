from sys import stdin, stdout

L = int(stdin.readline())
target = tuple(ord(c) - 96 for c in stdin.readline().rstrip())
num = [0, 1]
result = 0
while num[0] < L:
    result += target[num[0]] * num[1]
    num = [num[0] + 1, num[1] * 31]
stdout.write(f"{result % 1234567891}")
