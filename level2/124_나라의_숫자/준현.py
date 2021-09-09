

def solution(n):
    answer = ''
    temp = ['4', '1', '2']
    while n:
        answer += temp[n % 3]
        if n % 3:
            n //= 3
        else:
            n = n//3-1
    return answer[::-1]


print(solution(10))
