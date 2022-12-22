def solution(grid):
    answer = []
    vis = [[[False for _ in range(8)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # 상(out) : 0
    # 상(in) : 1
    # 좌(out) : 2 
    # 좌(in) : 3
    # 하(out) : 4
    # 하(in) : 5
    # 우(out) : 6
    # 우(in) : 7
    # 처음 시작은 1행 1열의 아무곳이나 잡고 시작
    # 다 구하고 나서 방문 하지 않은 곳 중 
    a = 0
    b = 0
    c = 1
    count = 0
    while True:
        if grid[a][b] == "L":
            if c + 2 > 7:
                c = 1
            else:
                c += 2
        elif grid[a][b] == "R":
            if c - 2 >= 0:
                c -= 2
            else:
                c = 7
        current_a = a
        current_b = b
        print((a,b))
        if c == 1:
            if a + 1 < len(grid):
                a += 1
            else:
                a = 0

        elif c == 3:
            if b + 1 < len(grid[0]):
                b += 1
            else:
                b = 0

        elif c == 5:
            if a - 1 >= 0:
                a -= 1
            else:
                a = len(grid) - 1
        elif c == 7:
            if b - 1 >= 0:
                b -= 1
            else:
                b = len(grid[0]) - 1
        after_c = c + 3
        if after_c > 7:
            after_c -= 8
        if not vis[a][b][c]:
            vis[current_a][current_b][after_c] = True
            vis[a][b][c] = True
            count += 1
        else:
            print(vis)
            break
                
            
            
    return count

print(solution(["SL","LR"]))