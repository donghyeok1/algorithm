def solution(plans):
    answer = []
    stk = []
    sorted_plans = sorted(plans, key=lambda x:(int(x[1].split(":")[0]), int(x[1].split(":")[1])))
    
    for plan_index in range(len(sorted_plans)):
        if plan_index < len(sorted_plans) - 1:
            next_plan_time = sorted_plans[plan_index + 1][1]
            next_hour, next_min = map(int, next_plan_time.split(":"))
            pre_hour, pre_min = map(int, sorted_plans[plan_index][1].split(":"))
            next_total_min = next_hour * 60 + next_min
            pre_total_min = pre_hour * 60 + pre_min
            sub = next_total_min - pre_total_min
            
            if sub >= int(sorted_plans[plan_index][2]):
                answer.append(sorted_plans[plan_index][0])
                pre = pre_total_min + int(sorted_plans[plan_index][2])
                while stk:
                    homework, rest_time = stk.pop()
                    if next_total_min >= pre + rest_time:
                        answer.append(homework)
                        pre += rest_time
                    else:
                        stk.append((homework, rest_time - (next_total_min - pre)))
                        pre += next_total_min - pre
                        break
            else:
                stk.append((sorted_plans[plan_index][0], int(sorted_plans[plan_index][2]) - sub))
        else:
            answer.append(sorted_plans[-1][0])
            
    while stk:
        answer.append(stk.pop()[0])
    
    return answer

