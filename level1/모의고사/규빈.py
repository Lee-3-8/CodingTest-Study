def solution(answers):
    answer = []
    cnt = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            cnt[0] += 1
        if answers[i] == two[i%len(two)]:
            cnt[1] += 1
        if answers[i] == thr[i%len(thr)]:
            cnt[2] += 1
    maxV = max(cnt)
    for i in range(3):
        if cnt[i] == maxV:
            answer.append(i+1)
    return answer