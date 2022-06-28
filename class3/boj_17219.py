from sys import stdin, stdout

N, M = map(int, stdin.readline().rstrip().split())
memory = {}
for _ in range(N):
    site, password = stdin.readline().rstrip().split()
    memory[site] = password
for _ in range(M):
    goal = stdin.readline().rstrip()
    stdout.write(f"{memory[goal]}\n")
