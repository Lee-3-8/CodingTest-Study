

def solution(s):
    s_list = []
    answer = 0
    for i in range(len(s)):
        s_list.append(s)
        s = s[1:]+s[0]
    for i in s_list:
        stack = []
        for j in i:
            if j == '[' or j == '{' or j == '(':
                stack.append(j)
            else:
                if stack:
                    if stack and (stack[-1] == '[' and j == ']') or (stack[-1] == '{' and j == '}') or (stack[-1] == '(' and j == ')'):
                        stack.pop()
                    else:
                        stack.append(j)
                else:
                    stack.append(j)

        if not stack:
            answer += 1
    return answer


s = "[](){}"
print(solution(s))
