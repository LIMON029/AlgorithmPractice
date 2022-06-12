from sys import stdin, stdout

BTNS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def getResult():
    global nowBtns, N
    count = abs(100 - N)
    for num in range(1000000):
        str_num = str(num)
        for index in range(len(str_num)):
            if int(str_num[index]) not in nowBtns:
                break
            elif index == len(str_num) - 1:
                count = min(count, abs(num - N) + len(str_num))
    stdout.write(f"{count}")


N = int(stdin.readline())
M = int(stdin.readline())
broken = [] if M == 0 else list(map(int, stdin.readline().split()))
nowBtns = [btn for btn in BTNS if btn not in broken]

getResult()
