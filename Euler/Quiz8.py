from itertools import permutations
import sys
import os

file_path = os.path.abspath(__file__)
txt_path = file_path[:-8] + 'q008_words.txt'
real_txt_path = txt_path.replace("\\", "/")

with open(real_txt_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

line = list()
for l in lines:
    line.append(l.strip()) 

result = set()

for word in line:
    ls = list(range(0,10))
    permute = permutations(ls, 4)
    
    for ls_pm in permute:
        if ls_pm[0] >= 3:
            coffee_word = 'COFFEE'
            coffee_set = set(coffee_word)
            answer = ''
            coffee_dict = {'C' : ls_pm[0], 'O' : ls_pm[1], 'F' : ls_pm[2], 'E' : ls_pm[3]}
            for words in coffee_word:
                answer += str(coffee_dict[words])
            answer = str(int(answer) * 3)
            
            if len(answer) == 7:
                text_word = ''
                new_dict = dict()
                for index in range(7):
                    if word[index] not in coffee_set:
                        if word[index] not in new_dict:
                            if int(answer[index]) not in coffee_dict.values() and int(answer[index]) not in new_dict.values():
                                new_dict[word[index]] = int(answer[index])
                                text_word += answer[index]
                            else:
                                break
                        else:
                            text_word += str(new_dict[word[index]])
                    else:
                        text_word += str(coffee_dict[word[index]])
                if text_word == answer:
                    result.add(word)
                    print(word)
                    if len(result) == 78:
                        print(word)
                        sys.exit()
