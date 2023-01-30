import sys

n = int(sys.stdin.readline())

tot = 2

for i in range(n):
    tot += tot - 1

print(tot**2)
