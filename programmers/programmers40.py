def bingo_count(board, word):
    bingo = 0
    # 행 검사
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == word:
                count += 1
        if count == 3:
            bingo += 1
    # 열 검사
    for i in range(3):
        count = 0 
        for j in range(3):
            if board[j][i] == word:
                count += 1
        if count == 3:
            bingo += 1
    # 대각선 검사
    if board[0][0] == word and board[1][1] == word and board[2][2] == word:
        bingo += 1
    elif board[2][0] == word and board[1][1] == word and board[0][2] == word:
        bingo += 1
    return bingo

def solution(board):
    answer = 1
    count_o = 0
    count_x = 0
    for i in range(3):
        count_o += board[i].count('O')
        count_x += board[i].count('X')
    
    if count_o > count_x + 1:
        return 0
    elif count_x > count_o:
        return 0
    elif count_o < 3:
        return 1
    else:
        x_bingo = bingo_count(board, "X")
        o_bingo = bingo_count(board, "O")
        if o_bingo > 0 and x_bingo == 0:
            if count_o > count_x:
                return 1
        elif o_bingo == 0 and x_bingo > 0:
            if count_o == count_x:
                return 1
        elif o_bingo == 0 and x_bingo == 0:
                return 1
        else:
            return 0
        return 0
        