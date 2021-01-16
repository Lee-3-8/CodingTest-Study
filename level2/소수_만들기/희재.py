import math
from itertools import combinations

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        answer += 1 if is_prime(sum(comb)) else 0
    return answer

if __name__ == '__main__':
    print(solution([1,2,7,6,4]))






'''
ㅅㅂ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;
'''