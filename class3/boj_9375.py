from sys import stdin, stdout
from collections import Counter

T = int(stdin.readline())
for _ in range(T):
    S = int(stdin.readline())
    case = []
    for _ in range(S):
        case.append(stdin.readline().rstrip().split()[1])
    counter = Counter(case)
    cnt = 1
    for key in counter:
        cnt *= counter[key] + 1
    stdout.write(f"{cnt-1}\n")
