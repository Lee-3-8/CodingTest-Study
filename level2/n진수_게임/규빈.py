def solution(n, t, m, p):
    answer = ''
    num = []
    for i in range(16):
        if i < 10:
            num.append(str(i))
        else:
            num.append(chr(ord('A') + i - 10))

    s = ''
    for i in range(t*m):
         s += changeType(i, n, num)
        
    for i in range(t):
        answer += ''.join(s[p - 1 + m*i].upper())

    return answer

def changeType(i, n, num):
    s = ''
    if i == 0:
        return '0'

    while(i>0):
        s = num[i%n] + s
        i = i//n
    return s