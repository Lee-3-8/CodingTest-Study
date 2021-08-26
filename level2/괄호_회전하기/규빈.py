def solution(s):
    answer = 0
    l = len(s)

    for i in range(l):
        after = s[:i]
        before = s[i:]
        string = before+after
        if iscorrect(string):
            answer += 1

    return answer

def iscorrect(s):
    symbols = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    openS = list(symbols.keys())
    stack = []
    for symbol in s:
        if symbol in openS:
            stack.append(symbol)
        else:
            if not stack or symbols[stack[-1]] != symbol:
                return False
            else:
                stack.pop()
    return False if stack else True