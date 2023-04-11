happy_cnt = 0
happy_sum = 0
for i in range(1, 10000):
    num_ls = list(str(i))
    visited = [False for _ in range(325)]
    while True:
        answer = 0
        for num in num_ls:
            answer += int(num) ** 2
        if answer == 1:
            happy_sum += i
            happy_cnt += 1
            break
        elif not visited[answer]:
            visited[answer] = True
            num_ls = list(str(answer))
        elif visited[answer]:
            break

print(happy_cnt * happy_sum)
