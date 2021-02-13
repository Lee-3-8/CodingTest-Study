# 3레벨     월간 코드 챌린지 시즌1      풍선 터트리기
# 최솟값을 밖에서 구해서 시간복잡도 O(n)으로 맞춤 나중에 다시풀어봐도 괜찮을 문제

from math import inf


def solution(a):
    result = 2
    l_list = [0] * len(a)
    l_min = inf
    r_list = [0] * len(a)
    r_min = inf

    for i in range(len(a)):
        if l_min > a[i]:
            l_min = a[i]
        l_list[i] = l_min

    for i in range(len(a) - 1, -1, -1):
        if r_min > a[i]:
            r_min = a[i]
        r_list[i] = r_min

    for i in range(1, len(a) - 1):
        if l_list[i - 1] > a[i] or r_list[i + 1] > a[i]:
            result += 1

    return result


# 처음 풀었던 방법 시간복잡도 와장창
# 9까지 맞고 시간초과
# def solution(a):
#     result = []

#     result.append(a[0])
#     result.append(a[-1])
#     l_min = a[0]
#     r_min = min(a[2:])
#     for i in range(1, len(a) - 1):
#         l_min = min(l_min, a[i - 1])
#         if a[i] == r_min:
#             r_min = min(a[i + 1 :])

#         print(l_min, r_min)
#         if l_min < a[i] and r_min < a[i]:
#             continue
#         else:
#             result.append(a[i])

#     return len(result)


# a = [9, -1, -5]
a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(a))
