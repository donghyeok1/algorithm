import itertools
def solution(users, emoticons):
    answer = []
    
    items = [10, 20, 30, 40]

    cases = list(itertools.product(items, repeat=len(emoticons)))

    for case in cases:
        cnt = 0
        total = 0
        for sale, limit in users:  
            user_total = 0
            for i in range(len(emoticons)):
                if sale <= case[i]:
                    user_total += emoticons[i] - emoticons[i] * case[i] * 0.01
            if user_total >= limit:
                cnt += 1
            else:
                total += user_total
        answer.append((cnt, total))
    
    answer = sorted(answer, reverse = True, key = lambda x : (x[0], x[1]))
    
    return answer[0]