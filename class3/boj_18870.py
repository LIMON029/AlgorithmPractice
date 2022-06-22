from sys import stdin, stdout

N = int(stdin.readline())
x_list = tuple(map(int, stdin.readline().rstrip().split()))
num_list = sorted(set(x_list))
dict_num = dict((num_list[i], i) for i in range(len(num_list)))
for x in x_list:
    stdout.write(f"{dict_num[x]} ")
