from sys import stdin, stdout


def getLine(lines, n):
    start, end = 1, max(lines)
    while start <= end:
        mid = (start + end) // 2
        line_cnt = 0
        for line in lines:
            line_cnt += line // mid

        if line_cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
    stdout.write(f"{end}")


K, N = map(int, stdin.readline().split())    # K: 가지고 있는 랜선 개수, N: 필요한 랜선 개수
myLine = []
for i in range(K):
    myLine.append(int(stdin.readline()))

getLine(myLine, N)
