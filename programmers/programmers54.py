def solution(name, yearning, photo):
    answer = []
    dic = dict()
    
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    
    for row in photo:
        total = 0
        for names in row:
            if names in dic:
                total += dic[names]
        answer.append(total)
    
    return answer