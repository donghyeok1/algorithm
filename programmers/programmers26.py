def solution(s):
    answer = 0
    temp = s
    dic = {"}" : "{", ")" : "(", "]" : "["}
    for i in range(len(s)):
        temp = s[i:] + s[0 : i]
        stack = []
        answer += 1
        flag = True
        for j in temp:
            for end, start in dic.items():
                if j == end:
                    if not stack:
                        flag = False
                        break
                    else:
                        a = stack.pop()
                        if a != start:
                            flag = False
                            break
            if not flag:
                answer -= 1
                break
            if j not in dic:
                stack.append(j)
                
        if stack and flag:
            answer -= 1

    return answer