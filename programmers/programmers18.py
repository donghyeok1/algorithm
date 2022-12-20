from collections import deque
def bfs(graph, visited, start):
    q = deque()
    q.append(start)
    visited[start] = True
    count = 1
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count
                   
def solution(n, wires):
    answer = n 
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        flag = False
        
        for j in range(len(wires)):
            if i != j:
                if not flag:
                    start = wires[j][0]
                    flag = True
                graph[wires[j][0]].append(wires[j][1])
                graph[wires[j][1]].append(wires[j][0])
        a = bfs(graph, visited, start)
        
        if answer > abs(n - 2 * a):
            answer = abs(n - 2 * a)
    
    return answer