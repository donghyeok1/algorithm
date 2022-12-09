from collections import Counter
def solution(k, tangerine):
    answer = 0
    dict_tan = dict(Counter(tangerine))
    dict_tan = sorted(dict_tan.items(), key = lambda x : x[1], reverse = True)
    
    for cnt in dict_tan:
        if k - cnt[1] <= 0:
            return answer + 1
        else:
            k -= cnt[1]
            answer += 1
    return answer