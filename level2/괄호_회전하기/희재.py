BRACKET = {")":"(", '}':'{', ']':'['}

def is_correct(s):
    stack = []
    for i in s:
        if len(stack) > 0 and i in BRACKET and BRACKET[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return not stack

def solution(s, answer=0):
    lotate = lambda x: x[1:] + x[0]
    for _ in range(len(s)):
        s = lotate(s)
        answer += is_correct(s)
    return answer

if __name__ == '__main__':
    print(solution("[](){}"))
