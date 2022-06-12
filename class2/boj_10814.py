from sys import stdin, stdout

N = int(stdin.readline())
members = []
for i in range(N):
    age, name = stdin.readline().split()
    members.append((int(age), name, i))

members.sort(key=lambda x: x[2])
for member in sorted(members, key=lambda x: x[0]):
    stdout.write(f"{member[0]} {member[1]}\n")
