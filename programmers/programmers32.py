def solution(s):
    answer = set()
    result = []
    set_ls = []
    temp = ""
    temp_ls = set()
    flag = False
    
    for i in s.split(","):
        temp = ""
        for w in i:
            if w != "{" and w != "}":
                temp += w
            if w == "}":
                flag = True
        temp_ls.add(int(temp))
        
        if flag:
            set_ls.append((temp_ls))
            temp_ls = set()
            flag = False
    
    set_ls = sorted(set_ls, key = len)
    
    for tup in set_ls:
        temp = tup - answer
        answer |= temp
        result.append(temp.pop())
    return result