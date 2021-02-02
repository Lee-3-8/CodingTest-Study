import re

def calc_time(start,end):
    s_hour, s_min = start.split(':')
    e_hour, e_min = end.split(':')

    return (int(e_hour)-int(s_hour))*60 + int(e_min) - int(s_min)

def solution(m, musicinfos):
    result = {}
    cnt = 0
    m = re.compile(r'[A-G][#]|[A-G]').findall(m)
    for v in musicinfos:
        start, end, title, music = v.split(',')
        run_t = calc_time(start, end)
        music = re.compile(r'[A-G][#]|[A-G]').findall(music)
        i=0
        while i != run_t:
            if music[i%len(music)] == m[cnt]:
                cnt += 1
            else:
                i -= cnt
                cnt = 0
            if cnt == len(m):
                result[title] = run_t
                cnt = 0
            i += 1
    return max(result, key=result.get) if result else "(None)"

print(solution(	"ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution(	"CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution(	"CDCDF", ["00:00,00:20,fuck,CDCDCDF"]))
# print(calc_time("13:50","14:00"))