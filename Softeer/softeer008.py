import sys
import heapq

n = int(sys.stdin.readline())

res = [0 for _ in range(n)]


for _ in range(3):
    ls = list(map(int, sys.stdin.readline().split()))
    heap = []
    rank = [0 for _ in range(n)]
    for i in range(n):
        res[i] += ls[i]
        heapq.heappush(heap, (-ls[i], i))
    
    i = 1
    equal_rank = 1
    for _ in range(n):
        score, index = heapq.heappop(heap)
        score = - score

        if heap:
            if heap[0][0] == - score:
                rank[index] = equal_rank
                i += 1
            else:
                rank[index] = equal_rank
                i += 1
                equal_rank = i
        else:
            rank[index] = equal_rank
    print(' '.join(map(str, rank)))

heap = []
for i in range(n):
    heapq.heappush(heap, (- res[i], i))

i = 1
rank = [0 for _ in range(n)]
equal_rank = 1

for _ in range(n):
    tot, ind = heapq.heappop(heap)
    tot = - tot
    if heap:
        if heap[0][0] == - tot:
            rank[ind] = equal_rank
            i += 1
        else:
            rank[ind] = equal_rank
            i += 1
            equal_rank = i
    else:
        rank[ind] = equal_rank
        
print(' '.join(map(str, rank)))
