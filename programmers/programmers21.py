from itertools import product
def solution(word): 
    w = ['A', 'E', 'I', 'O', 'U']
    ls = set()

    for i in range(1, 6):
        ls |= set(map("".join, product(w, repeat = i)))
        
    ls = sorted(list(ls))

    return ls.index(word) + 1
