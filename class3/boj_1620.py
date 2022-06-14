from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
pokemons = {}
for i in range(1, N+1):
    name = stdin.readline().rstrip()
    pokemons[name] = str(i)
    pokemons[str(i)] = name

result = []
for _ in range(M):
    now = stdin.readline().rstrip()
    result.append(pokemons[now])

result_str = "\n".join(result)
stdout.write(f"{result_str}")
