import heapq
from collections import defaultdict

def solution(N, road, K):
    cities = defaultdict(list)
    for start,end,weight in road:
        cities[start].append((weight,end))
        cities[end].append((weight,start))

    dist = [float('inf') for _ in range(N)]
    dist[0] = 0
    que = []
    heapq.heappush(que,[0,0])
    while que:
        cur_dist, cur_city = heapq.heappop(que)
        if dist[cur_city] < cur_dist: continue
        for weight,city in cities[cur_city+1]:
            if cur_dist + weight < dist[city-1]:
                dist[city-1] = cur_dist + weight
                heapq.heappush(que,[cur_dist+weight,city-1])

    return len(list(filter(lambda x:x<=K, dist)))

if __name__ =='__main__':
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))