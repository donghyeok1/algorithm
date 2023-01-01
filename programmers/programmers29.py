def solution(n):
    total = (n + 1) * n // 2
    ls = [[] for _ in range(n)]
    visited = [[] for _ in range(n)]
    for i in range(1, n + 1):
        ls[i - 1] = [0] * i
        visited[i - 1] = [False] * i
    nx, ny = 0, 0
    # 1 : 하
    # 2 : 우
    # 3 : 상
    flag = 1
    i = 2
    visited[0][0] = True
    ls[0][0] = 1
    while i <= total:
        if flag == 1:
            nx += 1
            if len(ls) <= nx or visited[nx][ny]:
                flag = 2
                nx -= 1
            else:
                ls[nx][ny] = i
                i += 1
                visited[nx][ny] = True
        elif flag == 2:
            ny += 1
            if len(ls[nx]) <= ny or visited[nx][ny]:
                flag = 3
                ny -= 1
            else:
                ls[nx][ny] = i
                i += 1
                visited[nx][ny] = True
        else:
            nx -= 1
            ny -= 1
            if (nx < 0 and ny < 0) or visited[nx][ny]:
                flag = 1
                nx += 1
                ny += 1
            else:
                ls[nx][ny] = i
                i += 1
                visited[nx][ny] = True
    
    
            
    return ls

solution(6)