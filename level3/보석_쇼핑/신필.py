
from collections import defaultdict

def solution(gems):
    gem_length = len(set(gems))
    left,right,buy = 0,float('inf'),defaultdict(int)
    l,r = 0,0
    while r < len(gems):
        while r < len(gems):
            buy[gems[r]]+= 1
            if len(buy) == gem_length:
                break
            r += 1
        while len(buy) == gem_length:
            buy[gems[l]]-= 1
            if buy[gems[l]] == 0:
                del buy[gems[l]]
                break
            l += 1
        left,right = (l,r) if r-l < right-left else (left,right)
        l += 1
        r += 1
    return left + 1, right + 1

if __name__ == '__main__':
    print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
    # print(solution(	["AA", "AB", "AC", "AA", "AC"]))