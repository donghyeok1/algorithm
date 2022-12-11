from collections import deque
def solution(queue1, queue2):
    result = 0
    sum_q1, sum_q2 = sum(queue1), sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    max_num = max(len(queue1), len(queue2)) + len(queue1) + len(queue2)
    
    if (sum_q1 + sum_q2) % 2 == 1:
        return -1
    
    elif sum_q1 == sum_q2:
        return 0
    
    while True:
        if result > max_num:
            return -1
        
        if sum_q1 == sum_q2:
            return result
        
        elif sum_q1 > sum_q2:
            a = queue1.popleft()
            sum_q1 -= a
            
            queue2.append(a)
            sum_q2 += a
            
        else:
            a = queue2.popleft()
            sum_q2 -= a
            
            queue1.append(a)
            sum_q1 += a
        
        result += 1