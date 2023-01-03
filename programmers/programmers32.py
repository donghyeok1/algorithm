def solution(s):
    answer = set()
    result = []
    set_ls = []
    flag = False
    
    s = s[2 : -2]
    
    for word_split in s.split("},{"):
        temp_ls = set()
        for final_split in word_split.split(","):
            temp_ls.add(int(final_split))
        set_ls.append(temp_ls)
        
    set_ls = sorted(set_ls, key = len)
    
    for tup in set_ls:
        temp = tup - answer
        answer |= temp
        result.append(temp.pop())

    return result