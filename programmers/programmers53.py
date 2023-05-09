def solution(players, callings):
    
    dic = dict()
    for rank in range(len(players)):
        dic[players[rank]] = rank

    for name in callings:
        cur_rank = dic[name]
        dic[name] -= 1
        tmp = players[cur_rank - 1]
        dic[tmp] += 1
        players[cur_rank - 1] = name
        players[cur_rank] = tmp
    return players