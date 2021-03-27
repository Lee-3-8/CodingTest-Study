def solution(number, k):
    stack = []
    cnt = 0
    for i in number:
        while stack and stack[-1] < i and cnt < k:
            stack.pop()
            cnt += 1
        stack.append(i)
    while cnt < k:
        stack.pop()
        cnt += 1
    string = ''.join(stack)
    return string