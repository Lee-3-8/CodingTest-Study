def solution(dartResult):
    a = list(dartResult)
    b = [] #계산할 숫자 리스트
    i = 0
    answer = 0

    while(len(a)): #dartResult를 리스트로 바꾸고 리스트 길이가 0일때까지 돌려
        s = a.pop(0)
        print(s)
        if (s >= '0' and s <= '9') : #숫자일때 
            num = int(s)
            if(a[0] == '0') : #뒷자리도 숫자이면
                s = a.pop(0)
                num = num*10 + int(s) #같이 계산
            b.append(num) #숫자 넣어주고
            i = i+1 #숫자일때만 i+1
        elif (s == 'D') :
            b[i-1] = b[i-1]**2
        elif (s == 'T') :
            b[i-1] = b[i-1]**3
        elif (s == '*') :
            if (i == 1) : #아직 한 자리만 채워졌으면 앞 *2
                b[i-1] *= 2
            else : #두 자리 이상 채워졌으면 앞앞, 앞 *2
                b[i-2] *= 2
                b[i-1] *= 2
        elif (s == '#') : #앞 - 곱하기
            b[i-1] *= (-1)
        
    answer = b[0] + b[1] + b[2] #계산
    return answer

print(solution('1D2S#10S'))
