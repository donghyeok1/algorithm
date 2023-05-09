def solution(park, routes):
    answer = []
    direction = {"E" : [0, 1], "S" : [1, 0], "W" : [0, -1], "N" : [-1, 0]}
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                current = [i, j]
    past = current[:]
    
    for route in routes:
        direct, num = route.split(" ")
        num = int(num)
        for _ in range(num):
            past[0] += direction[direct][0]
            past[1] += direction[direct][1]
            if 0 <= past[0] < len(park) and 0 <= past[1] < len(park[0]):
                if park[past[0]][past[1]] == "X":
                    past = current[:]
                    break
                else:
                    continue
            else:
                past = current[:]
                break
        else:
            current = past[:]
            
    return [current[0], current[1]]