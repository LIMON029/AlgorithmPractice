from sys import stdin, stdout
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    calc = stdin.readline().rstrip()
    n = int(stdin.readline())
    nums = deque(stdin.readline()[1:-2].split(","))
    if n == 0:
        nums = deque()
    done = True
    rev = 0
    for todo in calc:
        if todo == "R":
            rev += 1
        elif todo == "D" and nums:
            if rev % 2 == 0:
                nums.popleft()
            else:
                nums.pop()
        else:
            done = False
            break
    if done:
        if rev % 2 != 0:
            nums.reverse()
        stdout.write("["+",".join(nums)+"]\n")
    else:
        stdout.write("error\n")
