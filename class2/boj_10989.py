from sys import stdin, stdout

N = int(stdin.readline())
numList = [0] * 10001
for i in range(N):
    numList[int(stdin.readline())] += 1
for i in range(10001):
    for j in range(numList[i]):
        stdout.write(f"{i}\n")
