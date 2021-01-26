from collections import Counter

str1 = "E=M*C^2"
str2 = "e=m*c^2"


def solution(str1, str2):
    first_list = []
    second_list = []
    str1 = str1.lower()
    str2 = str2.lower()
    answer = 0
    inter = 0
    union = 0

    for i in range(len(str1)):
        temp = str1[i:i+2]
        if temp.isalpha() and len(temp) == 2:
            first_list.append(temp)
    for i in range(len(str2)):
        temp = str2[i:i+2]
        if temp.isalpha() and len(temp) == 2:
            second_list.append(temp)
    if not first_list and not second_list:
        return 65536
    c1 = Counter(first_list)
    c2 = Counter(second_list)
    # 굳이 dict로 안바꿔도 됌
    # set(first_dict.keys()) == set(first_dict) 차이?
    answer = int((sum((c1 & c2).values())/sum((c1 | c2).values()) * 65536))
    return answer


print(solution(str1, str2))
