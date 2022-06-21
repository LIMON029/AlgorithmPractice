from sys import stdin, stdout
import heapq as hq

N = int(stdin.readline())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            now = hq.heappop(heap)[1]
            stdout.write(f"{now}\n")
        else:
            stdout.write("0\n")
    else:
        hq.heappush(heap, (-x, x))
