def solution(rows, columns, queries):
    answer = []
    i = 1
    ls = []
    
    for j in range(rows):
        ls.append([k for k in range(i, i + columns)])
        i += columns
    for start_row, start_col, end_row, end_col in queries:
        garo = end_col - start_col + 1
        sero = end_row - start_row + 1
        
        ans = []
        tmp = ls[start_row][start_col - 1]
        ans.append(tmp)
        for i in range(garo):
            tmp1 = ls[start_row - 1][start_col - 1 + i]
            ls[start_row - 1][start_col - 1 + i] = tmp
            tmp = tmp1
            ans.append(tmp)
        for i in range(sero - 1):
            tmp1 = ls[start_row + i][end_col - 1]
            ls[start_row + i][end_col - 1] = tmp
            tmp = tmp1
            ans.append(tmp)
        for i in range(garo - 1):
            tmp1 = ls[end_row - 1][end_col - 2 - i]
            ls[end_row - 1][end_col - 2 - i] = tmp
            tmp = tmp1
            ans.append(tmp)
        for i in range(sero - 2):
            tmp1 = ls[end_row -2 - i][start_col - 1]
            ls[end_row -2 - i][start_col - 1] = tmp
            tmp = tmp1
            ans.append(tmp)
        answer.append(min(ans))
        
    return answer
