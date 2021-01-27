from collections import deque

def solution(cacheSize, cities):
    answer, cities = 0, [i.lower() for i in cities]
    cache = deque(maxlen=cacheSize)

    for city in cities:
        answer += 1 if city in cache else 5
        if city in cache:
            cache.remove(city)
        cache.append(city)
    return answer

if __name__ == '__main__':
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))