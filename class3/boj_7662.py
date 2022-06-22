from sys import stdin, stdout
import heapq as hq


def process(k):
    s_heap = []
    b_heap = []
    isReal = [False for _ in range(k)]
    for i in range(k):
        calc, num = stdin.readline().rstrip().split()
        num = int(num)
        if calc == 'I':
            hq.heappush(s_heap, (num, i))
            hq.heappush(b_heap, (-num, i))
            isReal[i] = True
        elif calc == 'D':
            if num > 0:
                while b_heap and not isReal[b_heap[0][1]]:
                    hq.heappop(b_heap)
                if b_heap:
                    isReal[b_heap[0][1]] = False
                    hq.heappop(b_heap)
            else:
                while s_heap and not isReal[s_heap[0][1]]:
                    hq.heappop(s_heap)
                if s_heap:
                    isReal[s_heap[0][1]] = False
                    hq.heappop(s_heap)

    while s_heap and not isReal[s_heap[0][1]]:
        hq.heappop(s_heap)
    while b_heap and not isReal[b_heap[0][1]]:
        hq.heappop(b_heap)

    if s_heap and b_heap:
        return " ".join([str(-b_heap[0][0]), str(s_heap[0][0])])
    else:
        return "EMPTY"


T = int(stdin.readline())
for _ in range(T):
    K = int(stdin.readline())
    result = process(K)
    stdout.write(f"{result}\n")
