def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if type == 2 else -degree
        temp[r1][c2 + 1] += -degree if type == 2 else degree
        temp[r2 + 1][c1] += -degree if type == 2 else degree
        temp[r2 + 1][c2 + 1] += degree if type == 2 else -degree
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            temp[i][j + 1] += temp[i][j]
    
    for j in range(len(board[0])):
        for i in range(len(board)):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            if board[i][j] > 0:
                answer += 1          
    return answer