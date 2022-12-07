import math

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        max_y = int(math.sqrt(math.pow(d, 2) - math.pow(x, 2)))
        answer += max_y // k + 1
    
    return answer