# 2레벨     코딩테스트 고득점 Kit     소수 찾기
from itertools import permutations
from collections import defaultdict


def solution(numbers):
    limit = 10 ** len(numbers)
    gp = [1] * limit
    gp[0] = gp[1] = 0
    dic = defaultdict(int)

    def prime(limit):
        for i in range(2, limit // 2):
            if gp[i] == 1:
                for j in range(i * 2, limit, i):
                    gp[j] = 0

    prime(limit)
    cnt = 0
    for i in range(1, len(numbers) + 1):
        t = set(permutations(numbers, i))
        for j in t:
            st = ""
            for q in j:
                st += q

            if gp[int(st)] == 1 and dic[int(st)] == 0:
                dic[int(st)] = 1
                cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution("011"))