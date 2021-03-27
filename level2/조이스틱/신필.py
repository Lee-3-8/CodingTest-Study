def get_min(name):
    result = -1
    for i in name:
        result+=1
        if i == 'A':
            result+=1
        elif ord(i) >= ord('N'):
            result += ord('Z') - ord(i)
            #z로 쪽으로
        else:
            result += ord(i) - ord('A')
            #a부터
        print(i,result)
    print('res',result)
    return result

def solution(name):
    norm = get_min(name)
    rev = get_min(name[::-1]) + 1

    return min(norm,rev)

print(solution("JAN"))