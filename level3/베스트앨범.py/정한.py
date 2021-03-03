#


def solution(genres, plays):
    g_tier = {}
    dic = {}
    result = []
    for i in range(len(genres)):
        if g_tier.get(genres[i]):
            g_tier[genres[i]] += plays[i]
        else:
            g_tier[genres[i]] = plays[i]

        if dic.get(genres[i]):
            dic[genres[i]].append((i, plays[i]))
        else:
            dic[genres[i]] = [(i, plays[i])]
    g_tier = sorted(g_tier.items(), key=lambda x: x[1], reverse=True)
    for i in g_tier:
        dic[i] = sorted(dic[i[0]], key=lambda x: (-x[1], x[0]))
        for idx, j in enumerate(dic[i]):
            if idx == 2:
                break
            result.append(j[0])
    return result


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
