def solution(line):
    answer = []
    cross = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            ad_bc = a * d - b * c
            bf_ed = b * f - e * d
            ec_af = e * c - a * f
            if ad_bc != 0:
                if bf_ed % ad_bc == 0 and ec_af % ad_bc == 0:
                    cross.append((bf_ed // ad_bc, ec_af // ad_bc))
                    
    cross_sero = sorted(cross, key = lambda x : x[1])
    cross_garo = sorted(cross)
    
    if cross_sero[0] == cross_sero[-1]:
        return ["*"]
    else:
        max_sero = cross_sero[-1][1] - cross_sero[0][1] + 1
        max_garo = cross_garo[-1][0] - cross_garo[0][0] + 1
        
        visited = [[False for _ in range(max_garo)] for _ in range(max_sero)]
        start_x = cross_garo[0][0]
        start_y = cross_sero[-1][1]
        
        for x, y in cross_sero:
            nx = x - start_x
            ny = start_y - y
            visited[ny][nx] = True
        
        for y in range(max_sero):
            tmp = ""
            for x in range(max_garo):
                if visited[y][x]:
                    tmp += "*"
                else:
                    tmp +="."
            answer.append(tmp)
    
    return answer