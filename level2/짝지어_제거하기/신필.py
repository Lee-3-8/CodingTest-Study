
def solution(s):
    stack = []
    for i in s:
        if stack:
            temp = stack.pop()
            if temp != i:
                stack.append(temp)
                stack.append(i)
        else: stack.append(i)
        print(stack , i)
    return 1 if not stack else 0


print(solution("baabaa"))
# print(solution("cdcd"))