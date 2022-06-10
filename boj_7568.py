from sys import stdin, stdout


def getRank(myList, now):
    rank = 1
    for student in myList:
        if now[0] < student[0] and now[1] < student[1]:
            rank += 1
    stdout.write(f"{rank} ")


N = int(stdin.readline())
students = []
for i in range(N):
    students.append(tuple(map(int, stdin.readline().split())))

for nowStudent in students:
    getRank(students, nowStudent)
