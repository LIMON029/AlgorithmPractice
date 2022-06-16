from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

no_listen = []
for _ in range(N):
    no_listen.append(stdin.readline().rstrip())
result = []
no_listen = set(no_listen)
for _ in range(M):
    name = stdin.readline().rstrip()
    if name in no_listen:
        result.append(name)
stdout.write(f"{len(result)}\n")
result_text = "\n".join(sorted(set(result)))
stdout.write(result_text)
