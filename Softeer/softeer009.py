import sys

n, b = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

a = sorted(a)

start = 1
end = 10 ** 9

while start < end:
    total = b
    mid = (start + end) // 2 + 1
    res = end

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
        end = mid - 1

print((start + end) // 2)