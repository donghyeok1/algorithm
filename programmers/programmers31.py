def rec(w):
    if w == "":
        return ""
    start = 0
    end = 0
    u = ""
    v = ""  
    
    for i in range(len(w)):
        if w[i] == "(":
            start += 1
        else:
            end += 1
        u += w[i]
        if start == end:
            if i != len(w) - 1:
                v = w[i + 1 : ]
                break
            else:
                v = ""
    stack = []
    flag = True
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                flag = False
                break
            else:
                stack.pop()
    if flag:
        # 올바른 문자열
        ans = rec(v)
        return u + ans
    else:
        # 올바르지 않은 문자열
        temp = "("
        ans = rec(v)
        temp = temp + ans + ")"
        new_u = u[1:-1]
        new_temp = ""
        for i in new_u:
            if i == "(":
                new_temp += ")"
            else:
                new_temp += "("
        temp += new_temp
        
        return temp
    
def solution(p):
    answer = rec(p)
    return answer