def solution(t, p):
    answer = 0
    len_p = len(p)
    for i in range(len(t)):
        if i + len_p - 1 < len(t):
            s = t[i : i + len_p]
            if int(s) <= int(p):
                answer += 1
        else:
            break
    return answer