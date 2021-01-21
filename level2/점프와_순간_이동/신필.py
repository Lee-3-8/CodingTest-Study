def solution(n):
    battery = 0
    while n!=0:
        print(n,battery)
        if n%2 == 0:
            n/=2
        else:
            n-= 1
            battery+=1
    return battery
print(solution(5000))