from collections import Counter
def solution(topping):
    answer = 0
    total_dic = dict(Counter(topping))
    brother_dic = dict()
    
    for i in range(len(topping)):
        if topping[i] not in brother_dic:
            brother_dic[topping[i]] = 1
        
        total_dic[topping[i]] -= 1

        if total_dic[topping[i]] == 0:
            del total_dic[topping[i]]
        
        if len(brother_dic) == len(total_dic):
            answer += 1
        
    return answer