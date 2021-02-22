from collections import Counter
from functools import reduce

def solution(clothes):
    temp = [x[1] for x in clothes]
    counter = Counter(temp)
    for i,v in counter.items():
        counter[i] = v + 1
    return reduce(lambda acc,cur: acc*cur, counter.values()) - 1

def solution2(clothes):
    temp = [x[1] for x in clothes]
    counter = Counter(temp)
    return reduce(lambda acc,cur: acc*(cur+1), counter.values(),1) - 1

print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))