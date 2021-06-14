from collections import defaultdict


def solution(n, results):
    n += 1
    answer = 0
    dic = [[False] * (n) for i in range(n)]

    for i in results:
        dic[i[0]][i[1]] = True

    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if dic[j][i] and dic[i][k]:
                    dic[j][k] = True

    for i in range(1, n):
        cnt = 0
        for j in range(1, n):
            if i == j:
                continue
            if dic[i][j] == True or dic[j][i] == True:
                cnt += 1
        if cnt == n-2:
            answer += 1
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))
