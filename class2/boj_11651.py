from sys import stdin, stdout

N = int(stdin.readline())
points = []
for i in range(N):
    points.append(tuple(map(int, stdin.readline().split())))

sortedY = sorted(tuple(points), key=lambda x: x[0])
for point in sorted(sortedY, key=lambda x: x[1]):
    stdout.write(f"{point[0]} {point[1]}\n")
