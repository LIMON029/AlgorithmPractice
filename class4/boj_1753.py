from sys import stdin, stdout
import heapq as hq

INF = 1e10


def DIJKSTRA(start):
    global V, graph
    heap = []
    distance = [INF for _ in range(V + 1)]
    distance[start] = 0
    hq.heappush(heap, (0, start))
    while heap:
        weight, node = hq.heappop(heap)
        for n_node, n_weight in graph[node]:
            if n_weight + weight < distance[n_node]:
                distance[n_node] = n_weight + weight
                hq.heappush(heap, (n_weight + weight, n_node))
    return distance


V, E = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(V + 1)]
K = int(stdin.readline())
for _ in range(E):
    u, v, w = map(int, stdin.readline().rstrip().split())
    graph[u].append([v, w])
result = DIJKSTRA(K)
for i in range(1, V + 1):
    for_print = result[i] if result[i] != INF else "INF"
    stdout.write(f"{for_print}\n")
