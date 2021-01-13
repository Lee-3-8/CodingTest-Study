def solution(s):
    s = s[2:-2].split("},{")
    s = list(map(lambda x: x.split(','), s))
    s.sort(key=lambda x: len(x))
    answer = []
    for i in s:
        for j in i:
            if not int(j) in answer:
                answer += [int(j)]
    return answer
