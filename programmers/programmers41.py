from collections import deque 
def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                start = (i, j)
                break
    q = deque()
    q.append((start ,0))
    
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[start[0]][start[1]] = True
    
    while q:
        pos, count = q.popleft()
        if board[pos[0]][pos[1]] == "G":
            return count
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            while True:
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] == "D":
                        if not visited[nx - dx[i]][ny - dy[i]]:
                            q.append(((nx - dx[i], ny - dy[i]), count + 1))
                            visited[nx - dx[i]][ny - dy[i]] = True
                            break
                        else:
                            break
                    else:
                        nx += dx[i]
                        ny += dy[i]
                else:
                    if not visited[nx - dx[i]][ny - dy[i]]:
                        q.append(((nx - dx[i], ny - dy[i]), count + 1))
                        visited[nx - dx[i]][ny - dy[i]] = True
                        break
                    else:
                        break
    return -1