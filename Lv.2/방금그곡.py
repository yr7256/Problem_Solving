from math import ceil


def solution(m, musicinfos):
    answer = '(None)'
    temp = 0
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
        start = start.split(':')
        end = end.split(':')
        s = int(start[0])*60+int(start[1])
        e = int(end[0])*60+int(end[1])
        m = m.replace('C#', 'c').replace('D#', 'd').replace(
            'F#', 'f').replace('G#', 'g').replace('A#', 'a')
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace(
            'F#', 'f').replace('G#', 'g').replace('A#', 'a')
        M = (melody*ceil((e-s)/len(melody)))[:(e-s)]
        if m in M and temp < e-s:
            answer = name
            temp = e-s
    return answer
