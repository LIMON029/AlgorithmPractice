# 시간 복잡도
# 리스트: O(n), 세트: O(1)

N = input()
A = set(input().split())
M = input()
B = input().split()

for num in B:
    print(1 if num in A else 0)
