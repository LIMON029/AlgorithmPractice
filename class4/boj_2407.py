from sys import stdin, stdout
from math import factorial

n, m = map(int, stdin.readline().rstrip().split())
stdout.write(f"{factorial(n) // (factorial(n-m) * factorial(m))}")
