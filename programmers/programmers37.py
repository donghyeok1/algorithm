def solution(keymap, targets):
    answer = []
    for word in targets:
        count = 0
        for alpha in word:
            min_key = 1000
            for keypad in keymap:
                key_index = keypad.find(alpha) + 1
                if key_index == 0:
                    continue
                min_key = min(key_index, min_key)
                if min_key == 1000:
                    count = -1
                    break
            if count == -1:
                break
            else:
                if min_key == 1000:
                    count = -1
                    break
                count += min_key
        if count == -1:
            answer.append(-1)
        else:
            answer.append(count)
    return answer