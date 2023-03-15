def solution(n, m, section):
    answer = 1
    if section[-1] - section[0] + 1  <= m:
        return answer
    
    next_pos = section[0] + m - 1
    for sect in section:
        if sect <= next_pos:
            continue
        else:
            next_pos = sect + m - 1
            answer += 1
    return answer