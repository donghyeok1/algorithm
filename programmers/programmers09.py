def solution(cards):
    answer = []
    i = 0
    total_sum = 0
    
    while total_sum != len(cards):
        temp = []
        start_i = i
        
        while cards[i] not in temp and cards[i] != -1:
            temp.append(cards[i])
            next_index = cards[i] - 1
            cards[i] = -1
            i = next_index
            
        if len(temp) != 0:
            answer.append(len(temp))
            
        i = start_i + 1
        total_sum += len(temp)
    
    if len(answer) == 1:
        return 0
    else:
        answer = sorted(answer, reverse = True)
        return answer[0] * answer[1]