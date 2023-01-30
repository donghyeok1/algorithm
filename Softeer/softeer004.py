import sys
import heapq

w, n = map(int, sys.stdin.readline().split())

ls = []
for i in range(n):
    total, kg = map(int, sys.stdin.readline().split())
    heapq.heappush(ls, (-kg, -total))

res = 0

for i in range(len(ls)):
    kg, tot = heapq.heappop(ls)
    kg = - kg
    tot = - tot
    if w >= tot:
        res += tot * kg
        w -= tot
    else:
        res += w * kg
        break

print(res)
