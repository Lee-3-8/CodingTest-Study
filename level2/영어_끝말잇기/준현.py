import math

words = ["hello", "one", "even", "never", "now", "world", "draw"]
n = 2


def solution(n, words):
    i = 0
    while True:
        if words[i] in words[:i]:
            return [i % n+1, math.ceil((i+1)/n)]
        elif i == len(words)-1:
            return [0, 0]
        elif words[i][-1] != words[i+1][0]:
            print(i)
            return [(i+1) % n+1, math.ceil((i+2)/n)]
        i += 1


print(solution(n, words))
