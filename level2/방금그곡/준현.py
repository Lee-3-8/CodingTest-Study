

m = "CCB"
musicinfos = ["03:00,03:2,FOO,CCB", "04:00,04:09,BAR,CCB"]


def change(song):
    if 'A#' in song:
        song = song.replace('A#', 'a')
    if 'C#' in song:
        song = song.replace('C#', 'c')
    if 'D#' in song:
        song = song.replace('D#', 'd')
    if 'F#' in song:
        song = song.replace('F#', 'f')
    if 'G#' in song:
        song = song.replace('G#', 'g')
    return song


def time_sort(music):
    music = change(music)
    temp = music.split(',')
    start = temp[0].split(':')
    end = temp[1].split(':')
    minutes = int(end[1])-int(start[1])
    hour = int(end[0])-int(start[0])
    time = hour*60+minutes
    temp.append(time)
    temp[3] = (temp[3]*time)[:time]

    return temp


def solution(m, musicinfos):
    m = change(m)
    musicinfos = change(musicinfos)
    music_list = []
    candidate_list = []
    for i in musicinfos:
        temp = time_sort(i)
        music_list.append(temp)
        print(music_list)
    for j in music_list:
        if m in j[3]:
            candidate_list.append([j[2], j[4]])
    print(candidate_list)
    if not candidate_list:
        return '(None)'
    elif len(candidate_list) == 1:
        return candidate_list[0][0]
    else:
        candidate_list = sorted(
            candidate_list, key=lambda x: x[1], reverse=True)
        return candidate_list[0][0]


print(solution(m, musicinfos))
