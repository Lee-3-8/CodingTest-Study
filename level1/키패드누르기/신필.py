#import math

pointMap = {
    '*': (-1, 0),
    '#': (1, 0),
    0: (0, 0),
    1: (-1, 3),
    2: (0, 3),
    3: (1, 3),
    4: (-1, 2),
    5: (0, 2),
    6: (1, 2),
    7: (-1, 1),
    8: (0, 1),
    9: (1, 1)
}

rpointMap = dict(map(reversed, pointMap.items()))

def getDistance(a,b):
    #return math.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2)) #싯팔 대각선으로 가도되는줄;;
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def solution(numbers, hand):
    Lfinger = '*'
    Rfinger = '#'
    numMap = {
        1: 'L',
        4: 'L',
        7: 'L',
        3: 'R',
        6: 'R',
        9: 'R'
    }
    answer = ''
    for num in numbers:
        result = numMap.get(num)
        if (not result): #numMap에서 none이 반환되면
            Ldistance = getDistance(pointMap.get(Lfinger),pointMap.get(num)) #왼손가락에서 num 사이의거리
            Rdistance = getDistance(pointMap.get(Rfinger),pointMap.get(num)) #오른손가락에서 num 사이의거리
            # 거리가 더가까운 손가락을 사용 , 같으면 주손가락으로
            result = hand.capitalize()[0] if Ldistance == Rdistance else ('L' if Ldistance < Rdistance else 'R')

        if(result == 'L'): Lfinger = num # 이동된 손가락정보를 update
        else : Rfinger = num

        answer += result #답안 문자열 만들기
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))