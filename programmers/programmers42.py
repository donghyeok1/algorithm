import math

def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        dis = []
        # 상
        height_white = n - startY
        bottom = abs(startX - x)
        height_black = n - y
        bottom_white = bottom * (height_white / (height_white + height_black))
        bottom_black = bottom * (height_black / (height_white + height_black))
        if bottom != 0:
            dis.append(round((math.sqrt(height_white ** 2 + bottom_white ** 2) + math.sqrt(height_black ** 2 + bottom_black ** 2)) ** 2, 2))
        else:
            if startY > y:
                dis.append((n - startY + n - y) ** 2)
            else:
                dis.append((startY + y) ** 2)
        # 하
        height_white = startY
        bottom = abs(startX - x)
        height_black = y
        bottom_white = bottom * (height_white / (height_white + height_black))
        bottom_black = bottom * (height_black / (height_white + height_black))
        if bottom != 0:
            dis.append(round((math.sqrt(height_white ** 2 + bottom_white ** 2) + math.sqrt(height_black ** 2 + bottom_black ** 2)) ** 2, 2))
        else:
            if startY > y:
                dis.append((n - startY + n - y) ** 2)
            else:
                dis.append((startY + y) ** 2)
        # 좌
        height_white = startX
        bottom = abs(startY - y)
        height_black = x
        bottom_white = bottom * (height_white / (height_white + height_black))
        bottom_black = bottom * (height_black / (height_white + height_black))
        if bottom != 0:
            dis.append(round((math.sqrt(height_white ** 2 + bottom_white ** 2) + math.sqrt(height_black ** 2 + bottom_black ** 2)) ** 2, 2))
        else:
            if startX > x:
                dis.append((m - startX + m - x) ** 2)
            else:
                dis.append((startX+ x) ** 2)
        # 우
        height_white = m - startX
        bottom = abs(startY - y)
        height_black = m - x
        bottom_white = bottom * (height_white / (height_white + height_black))
        bottom_black = bottom * (height_black / (height_white + height_black))
        if bottom != 0:
            dis.append(round((math.sqrt(height_white ** 2 + bottom_white ** 2) + math.sqrt(height_black ** 2 + bottom_black ** 2)) ** 2, 2))
        else:
            if startX > x:
                dis.append((m - startX + m - x) ** 2)
            else:
                dis.append((startX + x) ** 2)
        
        answer.append(min(dis))
            
    return answer
