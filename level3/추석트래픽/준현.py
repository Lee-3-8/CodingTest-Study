from datetime import time

lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]


def time_to_nano(i):
    take_time = int(float(i[2][:-1])*1000)
    nano = i[1].split('.')
    time = nano[0].split(':')
    sec = list(map(int, time))
    end = ((sec[0]*60+sec[1])*60+sec[2])*1000+int(nano[1])
    start = end-take_time+1
    return [start, end]


def check_rang(j, answer):
    cnt1 = 0
    cnt2 = 0
    start, end = j-999, j
    # for i in answer: 왜 한쪽만 실행?
    #     if i[1] >= start and i[0] <= end:
    #         cnt1 += 1
    start, end = j, j+999
    for i in answer:
        if i[1] >= start and i[0] <= end:
            cnt2 += 1
    return max(cnt1, cnt2)


def solution(lines):
    answer = []
    for i in lines:
        temp = time_to_nano(i.split())
        answer.append(temp)
    maxcnt = 0
    for i in answer:
        maxcnt = max(maxcnt, check_rang(
            i[0], answer), check_rang(i[1], answer))
    return maxcnt


print(solution(lines))
