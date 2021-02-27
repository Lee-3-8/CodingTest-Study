def solution(genres, plays):
    answer = []
    g = set(genres)
    dic = {}
    for genre in g:
        dic[genre] = []
    
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))
    
    total = []
    for key in dic:
        dic[key].sort(key = lambda x: (-x[1], x[0]))
        n = 0
        for index, num in dic[key]:
            n += num
        total.append((key, n))
    total.sort(key = lambda x: -x[1])

    for key, num in total:
        answer.append(dic[key][0][0])
        if len(dic[key]) > 1:
            answer.append(dic[key][1][0])

    return answer