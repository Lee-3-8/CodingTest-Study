def solution(N, stages):
    fail = [0 for i in range(N+1)]
    answer = []
    length = len(stages)
    for i in range(1, N+1):
        if length != 0:
            fail[i] = stages.count(i)/length
            length -= stages.count(i)
        else:
            fail[i] = 0
    max = -1
    index = 0
    for i in range(N):
        for idx, val in enumerate(fail):
            if max < val and idx != 0:
                max = val
                index = idx
        answer += [index]
        fail[index] = -1
        max = -1
    return answer
