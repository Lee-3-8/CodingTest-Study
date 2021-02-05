import re
from datetime import datetime, timedelta
def solution(lines):
    answer = 1
    times = []
    for i in range(len(lines)):
        cTime, pTime = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3} )(\d\.?\d*)', lines[i]).groups()
        endTime = datetime.strptime(cTime, '%Y-%m-%d %H:%M:%S.%f ')
        pTime = '2016-09-15 00:00:0' + str(float(pTime))
        processTime = datetime.strptime(pTime, '%Y-%m-%d %H:%M:%S.%f')
        startTime = endTime - processTime + timedelta(milliseconds=1)
        startTime = datetime(2016,9,15,0,0,0) + startTime
        times.append([startTime, endTime])
    times = sorted(times, key= lambda x : (x[1],x[0]))

    for i in range(len(times) - 1):
        for j in times[i]:
            later = j + timedelta(seconds=1) - timedelta(milliseconds=1)
            curNum = 1
            for k in range(i+1, len(times)):
                if later < times[k][0]:
                    break
                if (j <= times[k][0] and times[k][0] <= later) or (j <= times[k][1] and times[k][1] <= later) or (times[k][0] <= j and j <= times[k][1]):
                    curNum += 1
            answer = max(answer, curNum)

    return answer