from sys import stdin, stdout

N, M = map(int, stdin.readline().rstrip().split())
nums = list(map(int, stdin.readline().rstrip().split()))

nums_sum = []
last = 0
for num in nums:
    last = last + num
    nums_sum.append(last)


for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    if a > 1:
        stdout.write(f"{nums_sum[b-1] - nums_sum[a-2]}\n")
    else:
        stdout.write(f"{nums_sum[b-1]}\n")
