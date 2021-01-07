def solution(N, stages):
    answer = []
    roundN = []
    length = len(stages)
    dic = {}

    for i in range(N) : # 0으로 초기화
        roundN.append(0)

    for i in range(length) : # 인덱스에 인원수 넣어주기
        if(not (stages[i] - 1 >= N)) :
            roundN[stages[i] - 1] += 1

    for i in range(N) :
        sumN = 0
        for j in range(i) : # 이전 라운드까지의 사람수 구하기
            sumN += roundN[j]
        arrive = length - sumN # 현재라운드까지 도달한 사람수
        if(arrive == 0) : # 도달 한사람이 없으면 0
            dic[i + 1] = 0.0
        else :
            dic[i + 1] = roundN[i] / arrive # 실패율

    b = dict(sorted(dic.items(), key = lambda x: x[1], reverse=True))
    answer = list(b.keys())
    return answer

a = [4,4,4,4,4]
print(solution(4, a))