from datetime import timedelta
def get_time(time_string):
    h,m,s = time_string.split(':')
    return timedelta(hours=int(h),minutes=int(m),seconds=int(s))

def find_solution(start_arr, end_arr, start_time, end_time):
    cnt = 0
    for i in start_arr:
        if start_time <= i < end_time:
            cnt += 1
        else: break
    for i in end_arr:
        if  start_time <= i < end_time:
            cnt -= 1
        else: break
    return cnt

def get_time_arr(arr):
    start_arr = []
    end_arr = []
    for i in arr:
        start,end = i.split('-')
        start_arr.append(get_time(start))
        end_arr.append(get_time(end))
    start_arr.sort()
    end_arr.sort()
    return start_arr,end_arr
        

def solution(play_time, adv_time, logs):
    start_arr,end_arr = get_time_arr(logs)
    adv_time = get_time(adv_time)
    play_time = get_time(play_time)
    result = {}

    # 0부터 플레이타임까지 봐야함 0부터일때 예외처리 필수
    result[timedelta(seconds=0)] = find_solution(start_arr, end_arr,timedelta(seconds=0),adv_time)
    # i = 0
    # for i in start_arr:
    #     if i + adv_time > play_time: break
    #     result[i] = find_solution(start_arr, end_arr, i, i + adv_time)
    # print(result)
    # 사전에서 max값 찾아서 표시 

    # return result.max()



print(solution("02:03:55","00:14:15",["01:20:15-31:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))