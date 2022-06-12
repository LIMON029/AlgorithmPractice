from sys import stdout

N, K = map(int, input().split())

mans = list(range(1, N + 1))

index = K - 1
result = []
stdout.write("<")
while mans:
    stdout.write(f"{mans.pop(index)}")
    if mans:
        stdout.write(", ")
        N -= 1
        index = (index + K - 1) % N
stdout.write(">")
