from sys import stdin, stdout
from math import factorial

N = int(stdin.readline())
num = str(factorial(N))
flag = False
cnt = 0
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        cnt += 1
        flag = True
    elif flag and num[i] != '0':
        break
stdout.write(f"{cnt}\n")
