def solution(n,a,b):
    if a > b:
        a, b = b, a
    result = 1
    while not(b%2 == 0 and b-a == 1):
        print(a,b,result)
        result += 1
        a -= a // 2
        b -= b // 2
        
    return result

print(solution(8,1,8))