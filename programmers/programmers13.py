import math
from collections import defaultdict

def solution(fees, records):
    answer = defaultdict(int)
    basic_time = int(fees[0])
    basic_money = int(fees[1])
    minute_per = int(fees[2])
    minute_per_money = int(fees[3])
    record = dict()
    
    for rec in records:
        time, car_num, flag = rec.split()
        if flag == "IN":
            record[car_num] = time
        else:
            in_hour, in_minute = record[car_num].split(":")
            out_hour, out_minute = time.split(":")
            total_min = (int(out_hour) * 60 + int(out_minute)) - (int(in_hour) * 60 + int(in_minute))
            answer[car_num] += total_min
            del record[car_num]
    if len(record):
        for car_num, time in record.items():
            hour, minute = time.split(":")
            total_min = 1439 - (int(hour) * 60 + int(minute))
            answer[car_num] += total_min

    answer = dict(sorted(answer.items()))
    result = []
    for total_min in answer.values():
        if total_min > basic_time:
            fee = basic_money + math.ceil((total_min - basic_time) / minute_per) * minute_per_money
            result.append(fee)
        else:
            result.append(basic_money)
    return result


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))