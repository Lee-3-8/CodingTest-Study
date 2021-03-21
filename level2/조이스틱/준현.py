def solution(name):
    s = list(name)
    count = 0
    for a in s:
        if a == 'A':
            count += 1
    current = 0
    leftcount = 0
    rightcount = 0
    answer = 0
    if s[0] != 'A':
        answer += minus(s[0])
        s[0] = 'A'
        count += 1
    while True:
        if count == len(s):
            break
        i = current
        while s[i] == 'A':
            if i == len(s)-1:
                i = 0
            i += 1
            rightcount += 1
        j = current
        while s[j] == 'A':
            if j == 0:
                j += len(s)
            j -= 1
            leftcount += 1
        if rightcount <= leftcount:
            answer += rightcount
            current = i
            answer += minus(s[current])
        else:
            answer += leftcount
            current = j
            answer += minus(s[current])
        print(answer, s[current])
        leftcount = 0
        rightcount = 0
        s[current] = 'A'
        count += 1
    return answer


def minus(b):
    return min(abs(ord('A')-ord(b)), abs(ord(b)-ord('Z'))+1)


print(solution("JAN"))
