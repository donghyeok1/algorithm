def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i + 1)
        else:
            a = str(format(i, 'b'))
            zero_list = []
            for j in range(len(a)):
                if a[j] == "0":
                    zero_list.append(j)
            if not zero_list:
                ans = "10" + a[1:]
                answer.append(int(ans, 2))
            else:
                ans = a[:zero_list[-1]] + "10"
                if len(a) > zero_list[-1] + 2:
                    ans += a[zero_list[-1] + 2 :]
                answer.append(int(ans, 2))
    return answer