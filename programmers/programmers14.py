def solution(n, k):
    answer = 0
    trans = ""
    while n >= 1:
        n, b = divmod(n, k)
        trans += str(b)
        
    trans = trans[::-1]

    sosu_ls = []
    
    for num in trans.split("0"):
        if len(num) != 0 and num != "1":
            sosu_ls.append(int(num))

    for num in sosu_ls:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0 and i != 2:
                break
        else:
            answer += 1

    return answer