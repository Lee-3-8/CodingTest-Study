# 2020 카카오 인턴십    보석 쇼핑
from collections import defaultdict


def solution(gems):
    all_cnt = len(set(gems))
    s, e = 0, -1
    dic = defaultdict(int)
    cnt = 0
    min_len = float("inf")
    while not (len(gems) - 1 == e and cnt < all_cnt):
        if all_cnt == cnt:
            if min_len > e - s + 1:
                min_len = e - s + 1
                result = [s + 1, e + 1]

            else:
                dic[gems[s]] -= 1
                if dic[gems[s]] == 0:
                    cnt -= 1
                s += 1

        elif len(gems) - 1 != e:
            e += 1
            dic[gems[e]] += 1
            if dic[gems[e]] == 1:
                cnt += 1

    return result


if __name__ == "__main__":
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
