from datetime import datetime, timedelta

def convert_date(lines):
    result = []
    for line in lines:
        line_split = line.split()
        date_str = " ".join(line_split[:2])
        proc_time = line_split[-1][:-1]
        b_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        a_time = b_time - timedelta(seconds=float(proc_time) - 0.001)
        result.append((a_time, b_time))
    return result

def solution(lines):
    answer = 0
    lines = convert_date(lines)
    for idx, time in enumerate([i[1] for i in lines]):
        a_time = time - timedelta(microseconds=1)
        b_time = a_time + timedelta(seconds=1)
        proc_cnt = 0
        for proc in lines[idx:]:
            if proc[0] < b_time and proc[1] > a_time:
                proc_cnt += 1
        answer = max(answer, proc_cnt)

    return answer

if __name__ == '__main__':
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

'''
[
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
'''