import re
from datetime import datetime
def solution(m, musicinfos):
    answer = []
    
    m = changeMelody(m)

    for i in musicinfos:
        start, end, title, music = i.split(',')

        music = changeMelody(music)
        music = getRealPlay(start, end, music)

        p = re.search(f'{m}', music)
        if p:
            answer.append((len(music),title))
    
    if answer:
        maxIdx = 0
        for i in range(1, len(answer)):
            if answer[i][0] > answer[maxIdx][0]:
                maxIdx = i
        return answer[maxIdx][1]

    return "(None)"

def changeMelody(string):
    hashAlpa = {
        'C#':'c',
        'D#':'d', 
        'F#':'f', 
        'G#':'g', 
        'A#':'a'
        }
    for i in hashAlpa:
        string = string.replace(i, hashAlpa[i])
    
    return string

def getRealPlay(start, end, music):
    startTime = datetime.strptime(start, '%H:%M')
    endTime = datetime.strptime(end, '%H:%M')
    time = (endTime - startTime).seconds//60

    Len = len(music)
    i = time//Len
    if i:
        music *= i
        music += "".join(music[:time%Len])
    else:
        music = "".join(music[:time])
    return music