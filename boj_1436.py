from sys import stdin, stdout

N = int(stdin.readline())
cnt = 0
nowNum = 666
while cnt < N:
    if "666" in str(nowNum):
        cnt += 1
    nowNum += 1
stdout.write(str(nowNum - 1))
