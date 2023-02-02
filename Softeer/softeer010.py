import sys


num = {
    0 : set([0, 1, 2, 4, 5, 6]),
    1 : set([2, 5]),
    2 : set([0, 2, 3, 4, 6]),
    3 : set([0, 2, 3, 5, 6]),
    4 : set([1, 2, 3, 5]),
    5 : set([0, 1, 3, 5, 6]),
    6 : set([0, 1, 3, 4, 5, 6]),
    7 : set([0, 1, 2, 5]),
    8 : set([0, 1, 2, 3, 4, 5, 6]),
    9 : set([0, 1, 2, 3, 5, 6]),
    10 : set()
}



ls = [[0 for _ in range(11)] for _ in range(11)]
# 완전 꺼져있는 거는 10
t = int(sys.stdin.readline())

for i in range(11):
    for j in range(11):
        if i != j:
            if ls[i][j] == 0:
                pass

        

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    
    a, b = list(str(a)), list(str(b))
    if len(a) != 10:
        temp = 5 - len(a)
        a = ['10'] * temp + a
    
    if len(b) != 10:
        temp = 5 - len(b)
        b = ['10'] * temp + b
    total = 0
    for i in range(5):
        if a[i] == b[i]:
            continue
        else:
            total += len(num[int(b[i])] - (num[int(a[i])]) & num[int(b[i])]) + len(num[int(a[i])] - num[int(b[i])])
    print(total)