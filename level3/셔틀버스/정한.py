# 2018 KAKAO BLIND RECRUITMENT  [1차] 셔틀버스

from datetime import datetime, timedelta


def solution(n, t, m, timetable):
    time = [datetime.strptime(i, "%H:%M") for i in timetable]
    time.sort()
    idx = 0
    result = datetime.strptime("00:00", "%H:%M")
    start = datetime.strptime("09:00", "%H:%M")
    for i in range(n):
        now = start + timedelta(minutes=t * i)
        cnt = 0
        while idx < len(time) and time[idx] <= now and cnt < m:
            idx += 1
            cnt += 1

        if cnt < m:
            result = now
        else:
            result = time[idx - 1] - timedelta(minutes=1)

    return result.strftime("%H:%M")


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(
        solution(
            10,
            60,
            45,
            [
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
                "23:59",
            ],
        )
    )
