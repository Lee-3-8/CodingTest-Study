def solution(s):
    a = []
    for i in range(len(s)):
        if len(a) == 0:
            a.append(s[i])
        else:
            if s[i] == a[-1]:
                a.pop()
            else:
                a.append(s[i])

    if len(a):
        return 0
    else:
        return 1

print(solution("baabaa"))