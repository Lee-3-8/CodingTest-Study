from itertools import combinations as comb
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        combs = []
        for order in orders:
            combs.extend(sorted(map(lambda x: "".join(sorted(x)), comb(order, i))))
        counter = Counter(combs).most_common()
        for com, cnt in counter:
            if cnt == 1:
                break
            elif cnt == counter[0][1]:
                answer.append(com)

    return sorted(answer)

if __name__ == '__main__':
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
    print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))