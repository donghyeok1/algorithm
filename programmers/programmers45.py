def solution(cap, n, deliveries, pickups):
    answer = 0

    while deliveries or pickups:
        if deliveries[-1] != 0 or pickups[-1] != 0:
            break
        if deliveries and deliveries[-1] == 0:
            deliveries.pop()
        if pickups and pickups[-1] == 0:
            pickups.pop()

    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2
        if deliveries:
            if deliveries[-1] > cap:
                deliveries[-1] -= cap
            else:
                cnt = 0
                while deliveries and deliveries[-1] + cnt <= cap:
                    cnt += deliveries.pop()
                if deliveries:
                    deliveries[-1] -= cap - cnt
        if pickups:
            if pickups[-1] > cap:
                pickups[-1] -= cap
            else:
                cnt = 0
                while pickups and pickups[-1] + cnt <= cap:
                    cnt += pickups.pop()
                if pickups:
                    pickups[-1] -= cap - cnt
    return answer