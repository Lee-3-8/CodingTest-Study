import re


def solution(dartResult):
    number = re.compile("\d+")
    answer = number.findall(dartResult)
    answer = list(map(int, answer))

    alpha = re.compile("\D+")
    alpha_list = alpha.findall(dartResult)

    index = -1
    for j in alpha_list:
        index += 1
        print(answer)
        for i in j:
            if i == 'T':
                answer[index] **= 3
            elif i == 'D':
                answer[index] **= 2
            elif i == 'S':
                answer[index] **= 1
            elif i == '*':
                if index:
                    answer[index] *= 2
                    answer[index-1] *= 2
                else:
                    answer[index] *= 2
            else:
                answer[index] *= -1
    return sum(answer)
