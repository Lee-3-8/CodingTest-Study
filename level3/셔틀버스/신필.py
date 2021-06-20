from datetime import datetime, timedelta

def solution(n, t, m, timetable):
    interval = timedelta(minutes=t)
    start = datetime(2021,6,20,9)
    shuttle = []
    for _ in range(n): ## 셔틀 도착시간 리스트 생성
        shuttle.append([start.strftime('%H:%M'),0,start.strftime('%H:%M')]) # 셔틀도착시간,현재인원,마지막인원들어온시간
        start += interval

    timetable.sort()
    index = 0

    for i in range(len(shuttle)):
        while index < len(timetable) and shuttle[i][0] >= timetable[index] and shuttle[i][1] < m:
            shuttle[i][1] += 1 # 인원추가
            shuttle[i][2] = timetable[index] # 마지막들어온 사람 시간
            index += 1 # 다음 대기인원으로

    result = 0

    cur, cnt, last = shuttle[-1] # 마지막 셔틀확인

    if cnt == m:
        result = (datetime.strptime(last,'%H:%M') - timedelta(minutes=1)).strftime('%H:%M') # 꽉찼으면 한사람 떨구고 지가탐
    else:
        result = max(cur,last) # 자리남았으면 마지막사람들어온 시간 or 셔틀 도착시간중에 가장 느린시간에 탐
    return result

if __name__ == '__main__':
    # print(solution(	1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(	2, 10, 2, ["09:10", "09:09", "08:00"]))
