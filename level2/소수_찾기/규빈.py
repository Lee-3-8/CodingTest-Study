from itertools import permutations
import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    for i in range(1,len(numbers)+1):
        for tup in permutations(numbers, i):
            strNum = ''.join(tup)
            num = int(strNum)
            if num > 1 and isPrime(num):
                answer.add(num)

    return len(answer)