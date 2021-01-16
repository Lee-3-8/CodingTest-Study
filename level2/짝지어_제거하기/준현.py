def solution(s):
    stack = [s[0]]
    i = 1
    while i != len(s):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack += s[i]
        i += 1
    return 0 if stack else 1
