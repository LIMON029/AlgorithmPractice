N = int(input())
points = []
for i in range(N):
    points.append(tuple(map(int, input().split())))
points = sorted(tuple(points), key=lambda x:x[1])
for point in sorted(points, key=lambda x:x[0]):
    print(f"{point[0]} {point[1]}")
