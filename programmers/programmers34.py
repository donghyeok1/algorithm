def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = today.split(".")
    total_day = (int(today_year) - 2000) * 12 * 28 + int(today_month) * 28 + int(today_day)
    valid_dict = dict()
    
    for valid in terms:
        name, date = valid.split(" ")
        valid_dict[name] = date
    
    index = 0
    for privacy in privacies:
        index += 1
        p_date, p_name = privacy.split(" ")
        p_year, p_month, p_day = p_date.split(".")
        total_p_day = (int(p_year) - 2000) * 12 * 28 + int(p_month) * 28 + int(p_day)
        limit_day = int(valid_dict[p_name]) * 28
        
        sub_day = total_day - total_p_day
        
        if sub_day >= limit_day:
            answer.append(index)

    return answer