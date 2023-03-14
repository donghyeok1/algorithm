def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    for word in s:
        w_aski = ord(word)
        for _ in range(index):
            w_aski += 1
            while True:
                if w_aski > ord('z'):
                    w_aski = w_aski - ord('z') - 1 + ord('a')
                if chr(w_aski) not in skip:
                    break
                else:
                    w_aski += 1

        answer += chr(w_aski)
        
    return answer