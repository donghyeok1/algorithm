def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        share = (i + 1) // n
        remainder = (i + 1) % n
        if remainder == 0:
            answer.append(n)
        elif share + 1 >= remainder:
            answer.append(share + 1)
        else:
            answer.append(remainder)   
    return answer