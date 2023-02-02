import sys
import heapq

n, b = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

heap = []
for i in a:
    heapq.heappush(heap, (i, 0))

total = 0
while True:
    min_val, update = heapq.heappop(heap)
    if heap:
        if min_val <= heap[0][0]:
            total -= update ** 2
            if total + (update + 1) ** 2 == b:
                if min_val ==heap[0][0]:
                    print(min_val)
                else:
                    print(min_val + 1)
                break
            elif total + (update + 1) ** 2 < b:
                total += (update + 1) ** 2
                heapq.heappush(heap, (min_val + 1, update + 1))
            else:
                print(min_val)
                break

    else:
        res = b ** 0.5
        print(min_val + res)