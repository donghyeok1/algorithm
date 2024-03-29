import sys

n, b = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

a = sorted(a)

start = 1
end = (10 ** 9) * 2

while start + 1 < end:
    total = b
    mid = (start + end) // 2

    for i in range(len(a)):
        if mid <= a[i]:
            break
        total -= (mid - a[i]) ** 2
        if total < 0:
            break
    if total > 0:
        start = mid
    elif total == 0:
        break
    else:
        end = mid

print((start + end) // 2)