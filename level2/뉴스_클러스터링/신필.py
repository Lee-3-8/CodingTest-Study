from collections import Counter
import re

def cacl(big,small):
    if len(big) < len(small):
        big, small = small, big
    intersect = 0
    union = 0
    for key in big:
        b = big.get(key,0)
        s = small.get(key,0)
        union += b
        intersect += 0 if s == 0 else min(b, s)
    union += sum(small.values())
    union -= intersect
    return int(65536*intersect / union)

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    big = Counter([str1[i]+str1[i+1] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()])
    small = Counter([str2[i]+str2[i+1] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()])

    return 65536 if big == Counter() and small == Counter() else cacl(big,small)

# print(solution("FRANCE","french"))
# print(solution("handshake","shake hands"))
# print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))