import itertools
def solution(elements):
    answer = set(elements)
    
    for i in range(len(elements)):
        sum_el = elements[i]
        for j in range(1, len(elements)):
            next = i + j
            if next >= len(elements):
                next -= len(elements)
            sum_el += elements[next]
            answer.add(sum_el)
    
    return len(answer)
