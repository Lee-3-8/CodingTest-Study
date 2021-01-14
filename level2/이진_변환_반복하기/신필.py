
def solution(s):
    result = [0,0]
    while(s !='1'):
        print(s)
        result[0] += 1
        cnt = s.count('0')
        s = s.replace('0','',cnt)
        print(s,cnt)
        result[1] += cnt
        s = str(format(len(s),'b'))
    print(result)
    return result

solution("110010101001")
solution("01110")
solution("1111111")