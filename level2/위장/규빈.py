from collections import Counter

def solution(clothes):
    answer = 1
    t = []
    
    for i in clothes:
        t.append(i[1])
    a = Counter(t).values()

    for i in a:
        answer *= i+1
    return answer - 1