def digit(n,number):
    a = []
    while number>0: # 2진수구하기
        a.insert(0,number%2)
        number = number//2
    while n - len(a) > 0: # 0채워주기
        a.insert(0,0)
    return a

def solution(n, arr1, arr2):
    mapArr = []
    for i in range(n):
        map = ''
        answer1 = digit(n,arr1[i])
        answer2 = digit(n,arr2[i])
        for j in range(n):
            if answer1[j] + answer2[j] > 0:
                map += '#'
            else:
                map += ' '
            
        mapArr.append(map)
        
    return mapArr

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(5, arr1, arr2))