import sys
from collections import defaultdict

mes = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()

dic = defaultdict(int)

sec = [[0 for _ in range(5)] for _ in range(5)] 


r, c = 0, 0

for k in key:
    if c == 5:
        r += 1
        c = 0

    if dic[k] != 1:
        dic[k] = 1
        sec[r][c] = k
        c += 1

init = 'A'
while True:
    if c // 5 == 1:
        r += 1
        c = 0

    if r // 5 == 1:
        break
        
    if init == 'J':
        init = chr(ord(init) + 1)
        continue
    
    if dic[init] != 1:
        sec[r][c] = init
        dic[init] = 1
        c += 1
    
    init = chr(ord(init) + 1)


sec_mes = ""

i = 0
while i + 1 < len(mes):

    a, b = mes[i], mes[i + 1]
    if a == b:
        i += 1
        if a == "X":
            sec_mes += a + "Q"
        else:
            sec_mes += a + "X"
    else:
        i += 2
        sec_mes += a + b

if i == len(mes) - 1:
    sec_mes += mes[-1] + "X"


index = 0
real_mes = ""

while index + 1 < len(sec_mes):
    a, b = sec_mes[index], sec_mes[index + 1]
    
    for i in range(5):
        next_a = ""
        next_b = ""

        for j in range(5):
            if sec[i][j] == a:
                if j < 4:
                    next_a = sec[i][j + 1]
                else:
                    next_a = sec[i][0]
            if sec[i][j] == b:
                if j < 4:
                    next_b = sec[i][j + 1]
                else:
                    next_b = sec[i][0]
        if next_a != "" and next_b != "":
            real_mes += next_a + next_b
            index += 2
            break
    
    if next_a == "" or next_b == "":
        for k in range(5):
            next_a = ""
            next_b = ""

            for q in range(5):
                if sec[q][k] == a:
                    if q < 4:
                        next_a = sec[q + 1][k]
                    else:
                        next_a = sec[0][k]
                elif sec[q][k] == b:
                    if q < 4:
                        next_b = sec[q + 1][k]
                    else:
                        next_b = sec[0][k]
            if next_a != "" and next_b != "":
                real_mes += next_a + next_b
                index += 2
                break
                
        if next_a == "" or next_b == "":
            index += 2
            for s in range(5):
                for z in range(5):
                    if sec[s][z] == a:
                        pos_a = [s, z]
                    elif sec[s][z] == b:
                        pos_b = [s, z]
            real_mes += sec[pos_a[0]][pos_b[1]] + sec[pos_b[0]][pos_a[1]]


print(real_mes)
