def solution(n):
    result = ''
    nara_rule = [4,1,2]
    while n > 0:
        n,mod = divmod(n,3)
        result = str(nara_rule[mod]) + result
        if mod == 0: n-=1
    return result

if __name__ == '__main__':
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(10))

