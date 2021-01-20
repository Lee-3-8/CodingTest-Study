# 2017 팁스타운     짝지어 제거하기
# 스택을 활용하는 문제
# 스택 힌트 얻고 시간초과 해결했음 (다시 풀기)


# 정확성테스트 통과하고 효율성 통과 통과못한 솔루션
# n^2 시간이 걸리는것 같다
def solution1(s):
    answer = 0
    idx = 0

    while idx < len(s) - 1:
        if s[idx] == s[idx + 1]:
            if idx != 0:
                s = s[:idx] + s[idx + 2 :]
                idx -= 1

            else:
                s = s[2:]

        else:
            idx += 1

    print(s)
    return 1 if len(s) == 0 else 0


def solution(s):
    stack = []

    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 1 if len(stack) == 0 else 0


s = "baabaa"
# s = "cdcd"
# s = "ccddcdd"
print(solution(s))