# 2018 KAKAO BLIND RECRUITMENT      [3차] 방금그곡
# 스플릿을 이용한 문자열간 판별문제
# 정규표현식 이용
# l = sorted(l, key=lambda x: -x[4]) 역순정렬 안해줘서 2시간 + 리스트 2개인줄알고 1시간 날린 무제

import re


def solution(m, musicinfos):
    l = []
    for i in range(len(musicinfos)):
        temp = musicinfos[i].split(",")
        temp.append(time_check(temp[0], temp[1]))  # 재생시간
        l.append(temp)
    l = sorted(l, key=lambda x: -x[4])

    for i in l:
        if check(i, m) == 1:
            return i[2]

    return "(None)"


def time_check(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))

    return (end_h - start_h) * 60 + (end_m - start_m)


def sum_str(l, make_len):  # 재생길이만큼 늘려주는 함수
    len_l = len(l)
    temp = []
    for i in range(make_len):
        temp.append(l[i % len_l])

    return temp


def check(list, m):
    music = re.findall(r"[A-Z]#?", list[3])
    music = sum_str(music, list[4])
    m = re.findall(r"[A-Z]#?", m)

    for i in range(len(music) - len(m) + 1):
        if music[i : i + len(m)] == m:
            return 1

    return 0


"""
입출력 예시
"""
# m = "ABC"
# musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

m = "A#"
musicinfos = ["13:00,13:02,HAPPY,B#A#", "13:00,13:02,HELLO,B#A#"]  # HAPPY

# m = "CDEFGAC"
# musicinfos = ["12:00,12:06,HELLO,CDEFGA"]  # (None)

# m = "CCB"
# musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"] # FOO
print(solution(m, musicinfos))