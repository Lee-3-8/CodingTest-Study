from collections import deque

def solution(number, k):
    number_q = deque(number)
    i = 0
    while k != 0 and i != len(number_q)-2:
        print(number_q , f'num : {i} , {k}')
        if int(number_q[i]) < int(number_q[i+1]):
            del number_q[i]
            k -= 1
            i -= 1
        else:
            i+=1
        if i < 0 : i = 0
    while k != 0:
        number_q.pop()
        k -= 1

    return ''.join(number_q)


print(solution("1000", 3))
# print(solution("4177252841", 4))
# print(solution("21", 1))
