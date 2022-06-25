from sys import stdin, stdout
import heapq as hq

N = int(stdin.readline())
heap = []

for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            stdout.write(f"{hq.heappop(heap)[1]}\n")
        else:
            stdout.write("0\n")
    else:
        hq.heappush(heap, (x if x >= 0 else -x - 0.5, x))
