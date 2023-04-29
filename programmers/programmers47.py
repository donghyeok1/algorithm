def solution(n,a,b):
    answer = 0
    while True:
        if abs(b - a) == 1 and b // 2 != a // 2:
            return answer + 1
        else:
            if a % 2 == 1:
                a = a // 2 + 1
            else:
                a = a // 2
            if b % 2 == 1:
                b = b // 2 + 1
            else:
                b = b // 2
            answer += 1
    return answer
