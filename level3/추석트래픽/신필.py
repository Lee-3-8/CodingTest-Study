import datetime

def get_timeline(end_time,time):
    temp = end_time.split(':')
    e_timestamp = int(temp[0])*3600 + int(temp[1])*60 +float(temp[2])
    s_timestamp = e_timestamp - float(time[:-1])
    print(s_timestamp,e_timestamp)
    i = int(s_timestamp)
    result = []
    while i < e_timestamp:
        result.append(i)
        i += 1

    return result

def solution(lines):

    for i in lines:
        _, end_time, time = i.split(' ')
        end_time = datetime.datetime.strptime(end_time, '%H:%M:%S.%f')
        print(end_time,end_time.timestamp)
        # timeline = get_timeline(end_time,time)
        # for j in timeline:
        #     arr[j] += 1   
    return 1
# print(solution(["2016-09-15 00:00:00.000 3s"]))
# print(solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
# print(solution())
# print(solution())
# print(solution())
# print(solution())

