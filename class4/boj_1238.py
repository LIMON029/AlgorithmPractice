from sys import stdin, stdout
import heapq as hq

INF = 1e10


def DIJKSTRA(st, goal):
    global graph
    distance = {i: INF for i in range(1, N + 1)}
    heap = []
    hq.heappush(heap, (0, st))
    distance[st] = 0
    while heap:
        dist, node = hq.heappop(heap)
        if distance[node] < dist:
            continue
        for n_node in graph[node]:
            n_cost = dist + n_node[1]
            if n_cost < distance[n_node[0]]:
                distance[n_node[0]] = n_cost
                hq.heappush(heap, (n_cost, n_node[0]))
    return distance[goal]


N, M, X = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, stdin.readline().rstrip().split())
    graph[start].append((end, cost))

students_dist = []
for student in range(1, N+1):
    go_dist = DIJKSTRA(student, X)
    back_dist = DIJKSTRA(X, student)
    students_dist.append(go_dist+back_dist)

stdout.write(f"{max(students_dist)}")
