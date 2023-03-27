from collections import defaultdict, deque

def solution(picks, minerals):
    ls_dict = defaultdict(list)
    count_dia = 0
    count_iron = 0
    count_stone = 0
    for index in range(len(minerals)):
        if index == 0:
            pass
        elif index % 5 == 0:
            ls_dict['diamond'].append(count_dia)
            ls_dict['iron'].append(count_iron)
            ls_dict['stone'].append(count_stone)
            count_dia = 0
            count_iron = 0
            count_stone = 0
        else:
            pass
        count_dia += 1
        if minerals[index] == "diamond":
            count_iron += 5
            count_stone += 25
        elif minerals[index] == "iron":
            count_iron += 1
            count_stone += 5
        else:
            count_iron += 1
            count_stone += 1
    if count_dia != 0:
        ls_dict['diamond'].append(count_dia)
        ls_dict['iron'].append(count_iron)
        ls_dict['stone'].append(count_stone)
        
    q = deque()
    if picks[0] != 0:
        q.append(([picks[0] - 1, picks[1], picks[2]], 1, ls_dict['diamond'][0]))
    if picks[1] != 0:
        q.append(([picks[0], picks[1] - 1, picks[2]], 1, ls_dict['iron'][0]))
    if picks[2] != 0:
        q.append(([picks[0], picks[1], picks[2] - 1], 1, ls_dict['stone'][0]))
    result = list()    
    while q:
        pick, index, cnt = q.popleft()
        
        if index >= len(ls_dict['diamond']):
            result.append(cnt)
            continue
        elif pick[0] == pick[1] and pick[1] == pick[2] and pick[0] == 0:
            result.append(cnt)
            continue
        
        if pick[0] != 0:
            q.append(([pick[0] - 1, pick[1], pick[2]], index + 1, cnt + ls_dict['diamond'][index]))
        if pick[1] != 0:
            q.append(([pick[0], pick[1] - 1, pick[2]], index + 1, cnt + ls_dict['iron'][index]))
        if pick[2] != 0:
            q.append(([pick[0], pick[1], pick[2] - 1], index + 1, cnt + ls_dict['stone'][index]))
                
    return min(result)
