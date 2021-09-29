from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    maxV = [0] * (max(course)+1)
    dic = defaultdict(int)

    for n in course:
        for order in orders:
            for combi in combinations(order, n):
                combiString = ''.join(sorted(list(combi)))
                dic[combiString] += 1
                maxV[n] = max(maxV[n], dic[combiString])

    for key in dic.keys():
        if dic[key] == maxV[len(key)] and dic[key] >= 2:
            answer.append(key)

    return sorted(answer)