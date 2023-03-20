def solution(people, limit):
    people = sorted(people, reverse = True)
    count = 0
    start_index = 0
    end_index = len(people) - 1
    
    if start_index == end_index:
        return 1
    
    while start_index <= end_index:
        if start_index == end_index:
            count += 1
            break
        sum_person = people[start_index] + people[end_index]
        if sum_person > limit:
            start_index += 1
        else:
            start_index += 1
            end_index -= 1
        count += 1
        
    return count