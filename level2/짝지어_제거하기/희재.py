def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1


if __name__ == '__main__':
    result = solution("cdcd")
    print(result)
