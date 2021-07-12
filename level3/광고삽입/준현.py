from datetime import datetime, timedelta


def converse_type(time):
    i = list(map(int, time.split(':')))
    return timedelta(hours=i[0], minutes=i[1], seconds=i[2])


# 뺴기는 되는데 왜 플러슨 안될까..
def datetime_plus(start, end):
    return start + timedelta(hours=end.hour, minutes=end.minute, seconds=end.second)
    # start - end 는 가능

# 1 day, 8:37:27


def trans_timedelta(result):
    if "," not in str(result):
        i = str(result).split(':')
        st = i[0].zfill(2)+":"+i[1].zfill(2)+":"+i[2].zfill(2)
        return st
    else:
        i = str(result).split(' ')
        j = i[2].split(':')
        st = str(int(i[0])*24+int(j[0]))+":"+j[1]+":"+j[2]
        return st


def solution(play_time, adv_time, logs):
    play_time = converse_type(play_time)
    adv_time = converse_type(adv_time)
    log_list = []
    for i in logs:
        start, end = i.split('-')
        log_list.append([converse_type(start),
                         converse_type(end)])
    result_count = converse_type('00:00:00')
    result = converse_type('00:00:00')

    for i in log_list:
        if i[0] <= adv_time <= i[1]:
            result_count += adv_time-i[0]
        elif i[1] <= adv_time:
            result_count += i[1]-i[0]

    for j in range(len(log_list)):
        start, end = log_list[j][0], log_list[j][0]+adv_time
        count = converse_type('00:00:00')
        for i in log_list:
            if start <= i[0] and end <= i[0]:
                pass
            elif start >= i[1] and end >= i[1]:
                pass
            elif i[0] >= start and i[1] >= end:
                count += end-i[0]
            elif i[0] >= start and end >= i[1]:
                count += i[1]-i[0]
            elif i[0] <= start and i[1] >= end:
                count += end-start
            elif i[0] <= start and i[1] <= end:
                count += i[1]-start
        if result_count < count:
            result = start
            result_count = count
        elif result_count == count and result > start:
            result = start

    return trans_timedelta(result)
