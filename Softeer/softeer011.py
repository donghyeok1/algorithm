import sys

k, p, n = map(int, sys.stdin.readline().split())

for i in range(n):
    k = k * p % 1000000007

print(k)
