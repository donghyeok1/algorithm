from collections import Counter
def solution(want, number, discount):
    answer = 0
    sale = dict()
    for i in range(len(want)):
        sale[want[i]] = number[i]
        
    for i in range(len(discount)):
        if i + 10 <= len(discount):
            temp = dict(Counter(discount[i : i + 10]))
            if sale == temp:           
                answer += 1
        else:
            break
    return answer