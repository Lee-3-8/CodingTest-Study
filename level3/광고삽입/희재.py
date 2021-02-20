def to_sec(string):
    hours, minutes, seconds = string.split(":")
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

def to_str(sec):
    hours, remainder = divmod(sec, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def solution(play_time, adv_time, logs):
    play_time, adv_time = to_sec(play_time), to_sec(adv_time)
    sequences = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = map(to_sec, log.split('-'))
        sequences[start] += 1
        sequences[end] -= 1
    for i in range(1, len(sequences)):
        sequences[i] += sequences[i-1]

    max_range, answer = sum(sequences[:adv_time]), "00:00:00"
    cur_range = max_range
    for i in range(len(sequences) - adv_time):
        cur_range = cur_range - sequences[i] + sequences[i + adv_time]
        if cur_range > max_range:
            max_range, answer = cur_range, to_str(i + 1)

    return answer

if __name__ == '__main__':
    print(solution(	"99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))