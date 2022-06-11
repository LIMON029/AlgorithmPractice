from sys import stdin, stdout
#     0 1
# 0 : 1 0
# 1 : 0 1
# 2 : 1 1
# 3 : 1 2
# 4 : 2 3
# 5 : 3 5
# 6 : 5 8


def getZeroOneCount(n):
    zero, one = 1, 0
    for i in range(n):
        temp = zero
        zero = one
        one = temp + one
    stdout.write(f"{zero} {one}\n")


N = int(stdin.readline())
nums = []
for i in range(N):
    nums.append(int(stdin.readline()))
for num in nums:
    getZeroOneCount(num)
