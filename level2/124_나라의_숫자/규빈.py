from collections import deque
def solution(n):
    answer = deque()
    match = ['4', '1', '2']
    while n:
        answer.appendleft(match[n%3])
        if (n%3 == 0):
            n = n//3 - 1
        else:
            n = n // 3
    return ''.join(answer)