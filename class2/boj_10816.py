from sys import stdin, stdout
from collections import Counter

N = stdin.readline()
my_cards = sorted(tuple(map(int, stdin.readline().split())))
M = stdin.readline()
count_cards = tuple(map(int, stdin.readline().split()))

counter = Counter(my_cards)
for num in count_cards:
    stdout.write(f"{counter[num] if num in counter else '0'}")
    stdout.write(" " if num != [count_cards] else "\n")
