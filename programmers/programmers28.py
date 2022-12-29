def solution(storey):
    answer = 0
    res = int(storey)

    while True:
        if res == 0:
            break
        a = res % 10
        if a >= 6:
            answer += 10 - a
            res = res // 10 + 1
        elif a == 5:
            temp = res // 10
            b = temp % 10
            if b == 5 or b == 9:
                answer += 5
                res = res // 10 + 1
            else:
                answer += 5
                res = res // 10
        else:
            answer += a
            res = res // 10

    return answer
