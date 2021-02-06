import re
from datetime import datetime, timedelta
def solution(lines):
    answer = 0
    times = []
    for i in range(len(lines)):
        cTime, pTime = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} )(\d\.?\d*)', lines[i]).groups()
        endTime = datetime.strptime(cTime, '%Y-%m-%d %H:%M:%S.%f ')
        pTime = '2016-09-15 00:00:0' + str(float(pTime))
        processTime = datetime.strptime(pTime, '%Y-%m-%d %H:%M:%S.%f')
        startTime = endTime - processTime + timedelta(milliseconds=1)
        startTime = datetime(2016,9,15,0,0,0) + startTime
        times.append([startTime, i])
        times.append([endTime, i])

    for i in range(len(times) - 1):
        secLater = times[i][0] + timedelta(seconds=1) - timedelta(milliseconds=1)
        curNum = 1
        a = {times[i][1]}
        for j in range(i+1, len(times)):
            if times[j][1] not in a and secLater >= times[j][0]:
                curNum += 1
                a.add(times[j][1])
        answer = max(answer, curNum)

    return answer