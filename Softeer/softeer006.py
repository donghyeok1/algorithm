import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

room = []

dic = {}

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    room.append([name, 0, 0])
    dic[name] = list()



for _ in range(m):
    room_name, start, end = sys.stdin.readline().split()
    start, end = int(start), int(end)
    dic[room_name].append((start, end))

for k, v in dic.items():
    dic[k] = sorted(dic[k], key = lambda x : x[0])

dic = dict(sorted(dic.items()))


cnt = 0
for k, v in dic.items():
    cnt += 1
    start = 9
    print(f"Room {k}:")
    total = 0
    temp = []
    for st, en in v:
        if st > start:
            total += 1
            ran_st = start
            ran_en = st
            start = en
            if ran_st == 9:
                temp.append("09-" + str(ran_en))
            else:
                temp.append(str(ran_st) + "-" + str(ran_en))
        elif st == start:
            start = en
    if total:
        if start < 18:
            print(f"{total + 1} available:")
            temp.append(str(start) + "-18")
        else:
            print(f"{total} available:")
        for s in temp:
            print(s)
    else:
        if start < 18:
            print("1 available:")
            if start == 9:
                print(f"09-18")
            else:
                print(f"{start}-18")
        else:
            print("Not available")
    if cnt != len(dic):
        print("-----")
