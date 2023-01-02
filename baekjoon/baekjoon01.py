import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    command = sys.stdin.readline().rstrip()
    ls_len = int(sys.stdin.readline())
    input_ls = sys.stdin.readline().rstrip().split(',')
    ls = []
    for w in input_ls:
        temp = ""
        for j in w:
            if j != "[" and j != "," and j != "]":
                temp += j
        if temp:
            ls.append(int(temp))
    ls = deque(ls)
    flag = 1 # 1은 정방향, 0은 반대
    for word in command:
        if word == "R":
            if flag:
                flag = 0
            else:
                flag = 1
        else:
            if ls:
                if flag:
                    ls.popleft()
                else:
                    ls.pop()
            else:
                print("error")
                break
    else:
        if not flag:
            ls.reverse()
        print('['+','.join(map(str, ls))+']')