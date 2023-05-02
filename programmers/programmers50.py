def solution(targets):
    answer = 0
    
    targets = sorted(targets, key=lambda x : (x[0], x[1]))

    min_num = 10000000000
    
    prev_num = 0

    for target in targets:
        if target[1] <= min_num:
            min_num = target[1]

        if prev_num != target[0]:
            if min_num <= target[0]:
                answer += 1
                min_num = target[1]

        prev_num = target[0]
    
    return answer + 1
