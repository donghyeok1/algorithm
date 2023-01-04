from itertools import combinations
from collections import defaultdict
def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 
    for k in dic.keys():
        dic[k].sort()
    
                
    for q in queries:
        q = q.split(" and ")
        condition = ''.join(q[:-1]) + q[-1].split()[0]
        score = int(q[-1].split()[-1])
        if not len(dic[condition]):
            answer.append(0)
        else:
            start, end = 0, len(dic[condition]) - 1
            while start <= end:
                mid = (start + end) // 2
                if dic[condition][mid] >= score:
                    end = mid - 1
                else:
                    start = mid + 1
            answer.append(len(dic[condition]) - start)     
    return answer