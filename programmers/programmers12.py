from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    answer = dict()
    score = [i for i in range(0, 11)]
    
    apeech_dic = dict()
    apeech_sum_num = 0
    info.reverse()
    
    for i in range(len(info)):
        apeech_dic[i] = info[i]
        if info[i] != 0:
            apeech_sum_num += i
            
    max_num = 0

    for case in list(combinations_with_replacement(score, n)):
        lion_dic = dict(Counter(case))
        apeech_num = apeech_sum_num
        lion_num = 0
        
        for key, value in lion_dic.items():
            if lion_dic[key] > apeech_dic[key]:
                lion_num += key
                if apeech_dic[key] != 0:
                    apeech_num -= key
                    
        if lion_num > apeech_num:
            if max_num < lion_num - apeech_num:
                max_num = lion_num - apeech_num
                answer = lion_dic
                
    result = []         
    if len(answer) == 0:
        return [-1]
    else:
        for i in range(10, -1, -1):
            if i not in answer:
                result.append(0)
            else:
                result.append(answer[i])
            
        
    return result

