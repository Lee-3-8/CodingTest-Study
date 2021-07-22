# 2019 카카오 개발자 겨울 인턴십    징검다리 건너기
# 3회차
def solution(stones, k):
    # 이진탐색 -> 건널 수 있는 사람의 수
    l = 0
    r = max(stones) * k
    result = 0
    while l <= r:
        mid = (l + r) // 2
        check = 0
        for item in stones:
            if item < mid:
                check += 1
                if check == k:
                    break
            else:
                check = 0

        if check == k:  # 통과 못한 mid
            r = mid - 1
        else:  # mid 통과 (mid 늘려야함)
            result = max(result, mid)
            l = mid + 1
    return result


if __name__ == "__main__":
    print(solution([1, 1], 1))
