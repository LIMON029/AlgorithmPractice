from sys import stdin, stdout
import heapq as hq

INF = 1e10


def DIJKSTRA(start):
    global graph, N
    heap = []
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    hq.heappush(heap, (0, start))
    while heap:
        weight, node = hq.heappop(heap)
        for n_node in graph[node]:
            n_weight = weight + n_node[1]
            if n_weight < distance[n_node[0]]:
                distance[n_node[0]] = n_weight
                hq.heappush(heap, (n_weight, n_node[0]))
    return distance


N, E = map(int, stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, stdin.readline().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, stdin.readline().rstrip().split())
st_1 = DIJKSTRA(1)
st_v1 = DIJKSTRA(v1)
st_v2 = DIJKSTRA(v2)

result = min(st_1[v1] + st_v1[v2] + st_v2[N], st_1[v2] + st_v2[v1] + st_v1[N])
stdout.write(f"{result if result < INF else -1}")
