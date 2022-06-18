from sys import stdin
import heapq

heap = []
N = int(stdin.readline())
for _ in range(N):
    x = int(stdin.readline())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
