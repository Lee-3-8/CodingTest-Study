from collections import deque, defaultdict


def solution(s):
    result = 0
    s = deque(s)
    sym = defaultdict(
        int,
        {
            "]": "[",
            "}": "{",
            ")": "(",
        },
    )

    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == sym[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        if not stack:
            result += 1
        s.append(s.popleft())

    return result


if __name__ == "__main__":
    print(solution("[](){}"))