from collections import deque, defaultdict
from bisect import bisect_left

dic = defaultdict(int)
stack = deque()


def insert_q(b):
    if not stack:
        stack.append(b)
    else:
        temp = bisect_left(stack, b)
        stack.insert(temp, b)


def solution(operations):
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == 'I':
            if dic[b] == 0:
                insert_q(b)
                dic[b] += 1
            else:
                dic[b] += 1
        else:
            if b == 1 and stack:
                if dic[stack[-1]] == 1:
                    dic[stack[-1]] = 0
                    stack.pop()
                else:
                    dic[stack[-1]] -= 1

            if b == -1 and stack:
                if dic[stack[0]] == 1:
                    dic[stack[0]] = 0
                    stack.popleft()
                else:
                    dic[stack[0]] -= 1
    if stack:
        answer = [stack[-1], stack[0]]
    else:
        answer = [0, 0]
    return answer


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

print(solution(operations))
