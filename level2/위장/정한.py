# 2레벨     코딩테스트 고득점 Kit     위장
from itertools import combinations


def solution(clothes):
    dic = {}
    for i in clothes:
        if dic.get(i[1]) == None:
            dic[i[1]] = 1

        else:
            dic[i[1]] += 1

    result = list(dic.items())

    num = 1
    for i in [i[1] for i in result]:
        num *= i + 1

    return num - 1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))