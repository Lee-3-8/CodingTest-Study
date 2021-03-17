# 2레벨     코딩테스트 고득점 Kit     더 맵게
import heapq as hq


def solution(scoville, K):
    hq.heapify(scoville)

    cnt = 0
    while scoville[0] < K and len(scoville) >= 2:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        hq.heappush(scoville, a + b * 2)
        cnt += 1

    result = -1 if scoville[0] < K else cnt

    return result


if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
