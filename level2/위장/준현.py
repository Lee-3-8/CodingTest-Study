from collections import defaultdict
from itertools import combinations


def solution(clothes):
    dic = defaultdict(lambda: [])
    for i in clothes:
        dic[i[1]].append(i[0])
    temp = 1
    # dic = dict(map(len, dic))
    for i in dic:
        temp *= len(dic[i])+1

    return temp-1

    # def solution(clothes):
    #     answer = len(clothes)
    #     dic = defaultdict(lambda: [])
    #     for i in clothes:
    #         dic[i[1]].append(i[0])
    #     for i in range(2, len(dic.keys())+1):
    #         c = list(combinations(dic.keys(), i))
    #         for i in c:
    #             temp = 1
    #             for j in i:
    #                 temp *= len(dic[j])
    #             answer += temp


    #     return answer
clothes = [
    ["a", "aa"],
    ["b", "aa"],
    ["c", "aa"],
    ["a_a", "bb"],
    ["b_b", "bb"],
    ["c_c", "bb"],
    ["aaa", "cc"],
    ["bbb", "cc"],
    ["ccc", "cc"]

]

print(solution(clothes))
