def solution(k, ranges):
    answer = []
    sum_list = [0]
    while k != 1:
        prev_k = k
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        sum_list.append((prev_k + k) / 2 + sum_list[-1])
        
    end = len(sum_list) - 1
    
    for start, offset in ranges:
        range_end = end + offset
        if start == range_end:
            answer.append(0)
        elif start > range_end:
            answer.append(-1)
        else:
            answer.append(sum_list[range_end] - sum_list[start])
    return answer