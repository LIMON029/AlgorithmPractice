from sys import stdin, stdout

N = int(stdin.readline())
nums = {}
numList = []
max_cnt = 1
for i in range(N):
    num = int(stdin.readline())
    numList.append(num)
    if num in nums.keys():
        nums[num] += 1
        max_cnt = nums[num] if max_cnt < nums[num] else max_cnt
    else:
        nums.setdefault(num, 1)

numList = sorted(tuple(numList))
stdout.write(f"{round(sum(numList)/N)}\n")
stdout.write(f"{numList[N//2]}\n")
max_list = sorted((k for k, v in nums.items() if v == max_cnt))
stdout.write(f"{max_list[0] if len(max_list) < 2 else max_list[1]}\n")
stdout.write(f"{numList[-1] - numList[0]}\n")
