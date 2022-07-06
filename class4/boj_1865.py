from sys import stdin, stdout

INF = 1e10


def BellmanFord(nodeCnt, g):
    distance = [INF for _ in range(nodeCnt+1)]
    for n in range(1, nodeCnt+1):
        for e in range(1, nodeCnt+1):
            for n_node, n_time in g[e]:
                if distance[e] + n_time < distance[n_node]:
                    distance[n_node] = distance[e] + n_time
                    if n == nodeCnt:
                        return True
    return False


T = int(stdin.readline())

for _ in range(T):
    N, M, W = map(int, stdin.readline().rstrip().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, stdin.readline().rstrip().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for _ in range(W):
        S, E, T = map(int, stdin.readline().rstrip().split())
        graph[S].append([E, -T])

    result = "YES\n" if BellmanFord(N, graph) else "NO\n"
    stdout.write(result)
