def recul(start_row, start_col, n, arr, answer):
    if n == 1:
        return arr[start_row][start_col]
    n = n // 2
    a = recul(start_row, start_col, n, arr, answer)
    b = recul(start_row + n, start_col, n, arr, answer)
    c = recul(start_row, start_col + n, n, arr, answer)
    d = recul(start_row + n, start_col + n, n, arr, answer)
    if a == b and b == c and c == d and a != -1:
        return a
    else:
        if a != -1:
            answer[a] += 1
        if b != -1:
            answer[b] += 1
        if c != -1:
            answer[c] += 1
        if d != -1:
            answer[d] += 1
        return -1
    
def solution(arr):
    answer = [0, 0]
    d = recul(0, 0, len(arr), arr, answer)
    if d != -1:
        answer[d] += 1
    return answer