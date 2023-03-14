def solution(wallpaper):
    min_x, min_y = 50, 50
    max_x, max_y = 0, 0
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == "#":
                if min_x > x:
                    min_x = x
                if max_x < x:
                    max_x = x
                if min_y > y:
                    min_y = y
                if max_y < y:
                    max_y = y
    return [min_x, min_y, max_x + 1, max_y + 1]