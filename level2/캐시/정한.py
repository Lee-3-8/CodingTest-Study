# 2018 KAKAO BLIND RECRUITMENT      [1차] 캐시
# 데크 사용문제로 볼 수도 있으나 데크의 무작위 접근을 해야하는 문제이기 때문에
# 굳이 데크를 사용안함 ( 무작위 접근의 시간복잡도는 O(n) )
# LRU 알고리즘 사용 문제


def solution(cacheSize, cities):
    answer = 0
    queue = []
    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        t = i.upper()
        if t in queue:
            queue.remove(t)
            queue.append(t)
            answer += 1

        elif len(queue) == cacheSize:
            queue.pop(0)
            queue.append(t)
            answer += 5

        else:
            queue.append(t)
            answer += 5

    return answer


"""
입출력 예시
"""
# cacheSize = 3
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

# cacheSize = 2
# cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))
