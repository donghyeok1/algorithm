import math
def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2 + 1):
        green_inside_y = math.floor(math.sqrt(r2 ** 2 - x ** 2))
        blue_outside_y = math.ceil(math.sqrt(r1 ** 2 - x ** 2)) if r1 > x else 0
        
        answer += green_inside_y - blue_outside_y + 1
        
    return answer * 4