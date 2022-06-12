import sys

N = int(input())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

for num in sorted(nums):
    sys.stdout.write(f"{num}\n")