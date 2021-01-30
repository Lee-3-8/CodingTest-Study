from datetime import datetime
TIME = lambda x: datetime.strptime(x, "%M:%S")

def music_parse(melody):
    for i in ['C#','D#','F#','G#','A#']:
        melody = melody.replace(i, i[0].lower())
    return melody

def list_parse(musicinfos):
    music_list = []
    for info in musicinfos:
        src, dst, title, melody = info.split(",")
        melody = music_parse(melody)
        length = (TIME(dst) - TIME(src)).seconds
        melody = melody * (length // len(melody)) + melody[:length % len(melody)]
        music_list.append((title, melody, length))
    return music_list

def solution(m, musicinfos):
    m = music_parse(m)
    music_list = list_parse(musicinfos)
    answer, max_length = "(None)", 0
    for title, melody, length in music_list:
        if m in melody and length > max_length:
            answer, max_length = title, length
    return answer

if __name__ == '__main__':
    print(solution("ABC", ["00:00,00:06,HI,ABC#ABC"]))