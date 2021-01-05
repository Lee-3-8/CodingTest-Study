# 2018 KAKAO BLIND RECRUITMENT  [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        b1 = format(arr1[i], "b").zfill(n)
        b2 = format(arr2[i], "b").zfill(n)
        answer.append("")
        for j in range(n):
            if b1[j] == "0" and b2[j] == "0":
                answer[i] += " "

            else:
                answer[i] += "#"

    return answer


"""
출력 확인
"""
# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]

# n = 6
# arr1 = [46, 33, 33, 22, 31, 50]
# arr2 = [27, 56, 19, 14, 14, 10]

# print(solution(n, arr1, arr2))