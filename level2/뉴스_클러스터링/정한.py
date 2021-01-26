# 2018 KAKAO BLIND RECRUITMENT  [1차] 뉴스 클러스터링
# 문자열 슬라이싱 문제
# 문자열 알파벳 판별 함수 isalpha() 사용
from math import floor


def solution(str1, str2):

    list1, list2 = two_letter_slice(str1), two_letter_slice(str2)
    same_list, sum_list = [], []

    for i in list1:
        for idx, j in enumerate(list2):
            if i == j:
                same_list.append(i)
                del list2[idx]
                break
    sum_list = list1 + list2

    if len(sum_list) == 0 and len(same_list) == 0:
        answer = 65536
    else:
        answer = floor(len(same_list) / len(sum_list) * 65536)

    return answer


def two_letter_slice(str):
    result = []
    for i in range(len(str) - 1):
        temp = str[i : i + 2]
        if temp.isalpha():
            result.append(temp.upper())

    return result


"""
입출력 예시
"""
# str1 = "FRANCE"
# str2 = "french"

str1 = "aa1+aa2"
str2 = "AAAA12"
print(solution(str1, str2))