def solution(s):
    answer = []
    
    for string in s:
        stack = []
        cnt = 0

        for c in string:
            if c == '0' and len(stack) > 1 and stack[-2] == '1' and stack[-1] == '1':
                del stack[-2:]
                cnt += 1
            else:
                stack.append(c)
        
        if cnt == 0:
            answer.append(string)
        else:
            result = []

            while stack:
                if stack[-1] == '1':
                    result.append(stack.pop())
                else:
                    break
            
            result = ''.join(stack) + "110"*cnt + ''.join(result)

            answer.append(result)

    return answer