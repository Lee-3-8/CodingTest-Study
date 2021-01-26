from collections import deque
cachesize = 1
cities = ["SEOUL", "SEOUL", "SEOUL"]


def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0 or not cities:
        return len(cities)*5
    cities = list(map(lambda x: x.upper(), cities))

    cache = set()
    linked_cache = deque()
    for i in cities:
        if i in cache:
            linked_cache.remove(i)
            linked_cache.appendleft(i)
            answer += 1
        else:
            if cacheSize <= len(linked_cache):
                j = linked_cache.pop()
                cache.remove(j)
            linked_cache.appendleft(i)
            cache.add(i)
            answer += 5
    return answer


print(solution(cachesize, cities))
