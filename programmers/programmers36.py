def solution(cards1, cards2, goal):
    answer = ''
    card1_index, card2_index = 0, 0
    for word in goal:
        if card1_index < len(cards1) and cards1[card1_index] == word:
            card1_index += 1
        elif card2_index < len(cards2) and cards2[card2_index] == word:
            card2_index += 1
        else:
            return "No"
    answer = "Yes"
    return answer