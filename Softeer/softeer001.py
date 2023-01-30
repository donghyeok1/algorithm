import sys

total = 0
for i in range(5):
    start, end = sys.stdin.readline().split(" ")
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))

    if end_m >= start_m:
        total += (end_h - start_h) * 60 + end_m - start_m
    else:
        total += (end_h - start_h - 1) * 60 + end_m + 60 - start_m
print(total)
