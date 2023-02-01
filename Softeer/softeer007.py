import sys

n, m = map(int, sys.stdin.readline().split())

limit = []
base = []

for i in range(n):
    limit.append(list(map(int, sys.stdin.readline().split())))

for j in range(m):
    base.append(list(map(int, sys.stdin.readline().split())))

i = 0
res = []
for leng, ver in limit:
    while i < len(base):
        if leng > base[i][0]:
            leng -= base[i][0]
            if ver >= base[i][1]:
                res.append(0)
            else:
                res.append(base[i][1] - ver)
            i += 1
        elif leng < base[i][0]:
            base[i][0] -= leng
            if ver >= base[i][1]:
                res.append(0)
                break
            else:
                res.append(base[i][1] - ver)
                break
        else:
            if ver >= base[i][1]:
                res.append(0)
            else:
                res.append(base[i][1] - ver)
            i += 1
            break
print(max(res))
