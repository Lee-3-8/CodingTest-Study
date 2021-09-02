
def mv(temp):
    stack = []
    more = ['1', '1', '0']
    cnt = 0
    for i in temp:
        if i == '0' and stack[-2:] == ['1', '1']:
            cnt += 1
            stack.pop()
            stack.pop()
        else:
            stack.append(i)
    cnt2 = 0
    stack_len = len(stack)
    answer = []
    if cnt != 0:
        for i in stack:
            if i == '1' and cnt2+1 < stack_len and stack[cnt2+1] == '1':
                answer = stack[:cnt2] + cnt*more + stack[cnt2:]
                answer = "".join(answer)
                break
            cnt2 += 1
        if not answer:
            if '0' in stack:
                cnt3 = 0
                for i in stack[::-1]:
                    if i == '0':
                        answer = stack[:stack_len-cnt3] + \
                            cnt*more + stack[stack_len-cnt3:]
                        answer = "".join(answer)
                        break
                    cnt3 += 1
            else:
                answer = cnt*more+stack
                answer = "".join(answer)
        return answer
    else:
        return temp


def solution(s):
    answer = [mv(i) for i in s]
    return answer


s = ["1110", "100111100", "0111111010"]
print(solution(s))
