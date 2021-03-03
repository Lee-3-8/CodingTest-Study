from collections import defaultdict
from heapq import heappop, heappush

def solution(genres, plays):
    infos = defaultdict(lambda : {'total':0, 'plays':[]})
    for idx, (gen, play) in enumerate(zip(genres, plays)):
        infos[gen]['total'] += play
        heappush(infos[gen]['plays'], (-play, idx))

    answer = []
    infos = sorted(infos.items(), key=lambda x: x[1]['total'], reverse=True)
    for _, info in infos:
        answer.append(heappop(info['plays'])[1])
        if info['plays']:
            answer.append(heappop(info['plays'])[1])

    return answer

if __name__ == '__main__':
    print(
        solution(
            ["classic", "pop", "classic", "classic",],
            [500, 600, 150, 800,]

        )
    )