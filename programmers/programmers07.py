def solution(order):
    answer = 0
    stack = []
    start = 1
    for box in order:
        if box not in stack:
            for i in range(start, box):
                stack.append(i)
            start = box + 1
            answer += 1
        else:
            if stack[-1] == box:
                stack.pop()
                answer += 1
            else:
                break
    return answer