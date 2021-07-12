# 2021 KAKAO BLIND RECRUITMENT  광고 삽입
import re


def solution(play_time, adv_time, logs):
    def time_check(log):  # 초로 변환
        if len(log) == 8:
            s = re.findall(r"[0-9]+", log)
            s = int(s[0]) * 60 * 60 + int(s[1]) * 60 + int(s[2])
            return s
        s, e = re.split(r"-", log)
        s = re.findall(r"[0-9]+", s)
        e = re.findall(r"[0-9]+", e)
        s = int(s[0]) * 60 * 60 + int(s[1]) * 60 + int(s[2])
        e = int(e[0]) * 60 * 60 + int(e[1]) * 60 + int(e[2])
        return s, e

    end_time = time_check(play_time)
    adv_len = time_check(adv_time)
    dp = [0] * (end_time + 1)

    for log in logs:
        s, e = time_check(log)
        dp[s] += 1
        dp[e] -= 1

    state = 0  # 현재 보는 시청수
    time = 0
    s, e = 0, 0
    result = [0, 0]  # 시작시간, 누적재생시간
    print(time_check("00:14:15"))
    while e <= end_time:
        while e <= end_time and e - s < adv_len:
            state += dp[e]
            time += state
            e += 1
            if time > result[1]:
                result[0] = s
                result[1] = time
        s += 1

    print(result)
    print(time_check("01:30:59"))


if __name__ == "__main__":
    print(
        solution(
            "02:03:55",
            "00:14:15",
            [
                "01:20:15-01:45:14",
                "00:40:31-01:00:00",
                "00:25:50-00:48:29",
                "01:30:59-01:53:29",
                "01:37:44-02:02:30",
            ],
        )
    )
