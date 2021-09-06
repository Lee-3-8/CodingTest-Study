from collections import deque
def solution(s):
    answer = []
    
    for string in s:
        stack = []
        cnt = 0

        for c in string:
            if c == '0' and len(stack) > 1 and stack[-2] == '1' and stack[-1] == '1':
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(c)
        
        if cnt == 0:
            answer.append(string)
        else:
            result = deque()

            while stack:
                if stack[-1] == '1':
                    result.append(stack.pop())
                else:
                    break

            while cnt > 0:
                result.appendleft('0')
                result.appendleft('1')
                result.appendleft('1')
                cnt -= 1

            while stack:
                result.appendleft(stack.pop())

            answer.append(''.join(result))

    return answer