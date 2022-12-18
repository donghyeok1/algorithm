answer = 0
vis = []

def dfs(rest_k, count, dungeons):
    global answer
    if answer < count:
        answer = count
    for flag in range(len(vis)):
        if not vis[flag]:
            if rest_k >= dungeons[flag][0]:
                vis[flag] = True
                dfs(rest_k - dungeons[flag][1], count + 1, dungeons)
                vis[flag] = False
                
def solution(k, dungeons):
    global vis
    vis = [False for _ in range(len(dungeons))]
    dfs(k, 0, dungeons)
    return answer