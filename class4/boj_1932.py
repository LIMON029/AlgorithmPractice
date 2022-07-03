from sys import stdin, stdout

n = int(stdin.readline())

triangle = [0 for _ in range(n*(n+1)//2)]
index = 0
for i in range(n):
    now = list(map(int, stdin.readline().rstrip().split()))
    if i == 0:
        triangle[i] = now[0]
        continue
    if i == 1:
        triangle[i] = triangle[i-1] + now[0]
        triangle[i+1] = triangle[i-1] + now[1]
        index += 1
        continue
    cnt = 0
    for num in now:
        if cnt == 0:
            triangle[(i*(i+1))//2+cnt] = triangle[index] + num
        elif cnt == i:
            triangle[(i*(i+1))//2+cnt] = triangle[index-1] + num
        else:
            triangle[(i*(i+1))//2+cnt] = max(triangle[index], triangle[index-1]) + num
        cnt += 1
        if cnt != i + 1:
            index += 1

stdout.write(f"{max(triangle[-n:])}")
