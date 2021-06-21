from collections import deque

def refine_timetable(timetable, last_bus):
    refined = deque()
    timetable.sort()
    for time_i in timetable:
        t = int(time_i.split(":")[0]) * 60 + int(time_i.split(":")[1])
        if last_bus < t:
            break
        refined.append(t)
    return refined

def solution(n, t, m, timetable):
    bus_table = deque([540 + i * t for i in range(n)])
    user_table = refine_timetable(timetable, bus_table[-1])
    sheets, last_user = m, None

    while bus_table and user_table:
        while sheets and user_table and user_table[0] <= bus_table[0]:
            last_user = user_table.popleft()
            sheets -= 1
        bus_table.popleft()
        sheets = m
    if bus_table:
        return '%02d:%02d' % (bus_table[-1] // 60, bus_table[-1] % 60)
    else:
        return '%02d:%02d' % ((last_user - 1) // 60, (last_user - 1) % 60 )


if __name__ == '__main__':
    print(solution(
        1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
    ))