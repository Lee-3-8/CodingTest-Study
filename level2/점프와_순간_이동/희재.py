def solution(n):
    return format(n, 'b').count('1')

if __name__ == '__main__':
    print(solution(5))

'''
def solution(n):
    answer = 0
    while n:
        answer += n % 2
        n //= 2
    return answer
'''