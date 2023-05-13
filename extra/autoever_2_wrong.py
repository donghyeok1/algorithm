import sys

N = int(sys.stdin.readline())

dic_set = set()
dic_ls = list()
answer = ["No"] * N

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    dic_set.add(word)
    dic_ls.append(word)

for i in range(N):
    for j in range(N):
        if dic_ls[i] in dic_ls[j]:
            start = dic_ls[j].index(dic_ls[i])
            end = start + len(dic_ls[i]) - 1
            if start == 0 or end == len(dic_ls[j]) - 1:
                continue
            else:
                tmp_word = dic_ls[j][ : start] + dic_ls[j][end + 1 : ]
                if tmp_word in dic_set:
                    answer[j] = "Yes"
                else:
                    end_other = end
                    while True:
                        front_word = dic_ls[j][ : end_other + 1]
                        other_case = dic_ls[j][end_other + 1 : ]
                        if dic_ls[i] in other_case:
                            start = other_case.index(dic_ls[i])
                            end = start + len(dic_ls[i]) - 1
                            if end != len(other_case) - 1:
                                tmp_word = front_word + other_case[ : start] + other_case[end + 1 : ]
                                if tmp_word in dic_set:
                                    answer[j] = "Yes"
                                    break
                                else:
                                    end_other += end
                            else:
                                break
                        else:
                            break
for i in range(N):
    print(answer[i])