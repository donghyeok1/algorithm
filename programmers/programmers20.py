def solution(data, col, row_begin, row_end):
    answer = 0
    ls = []
    data = sorted(data, key = lambda x : (x[col - 1], -x[0]))
    data = data[row_begin - 1 : row_end]

    for d in data:
        s = 0
        for a in d:
            s += a % row_begin
        
        if not ls:
            ls.append(s)
        else:
            ls[0] = ls[0] ^ s
        row_begin += 1
    
    return ls[0]