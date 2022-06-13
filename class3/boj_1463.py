from sys import stdin, stdout

N = int(stdin.readline())

prev = [0 for _ in range(N + 1)]

for num in range(2, N + 1):
    prev[num] = prev[num - 1] + 1

    if num % 2 == 0:
        prev[num] = min(prev[num], prev[num // 2] + 1)
    if num % 3 == 0:
        prev[num] = min(prev[num], prev[num // 3] + 1)

stdout.write(f"{prev[N]}")