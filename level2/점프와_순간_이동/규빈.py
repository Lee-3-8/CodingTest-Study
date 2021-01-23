def solution(n):
    return loof(n)

def loof(n):
    if n <= 2 :
        return 1
    if n%2==1:
        return loof(n//2)+1
    else:
        return loof(n//2)