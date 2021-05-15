from collections import deque


def trans(target):
    arr = set()
    for i in range(len(target)):
        for j in range(97, 123):
            arr.add(target[0:i]+chr(j)+target[i+1:])
    return arr


def solution(begin, target, words):
    if target not in set(words):
        return 0
    queue = deque()
    queue.append((begin, 0))
    check = [0]*len(words)
    while queue:
        t, c = queue.popleft()
        if t == target:
            return c
        temp = trans(t)
        for idx, val in enumerate(words):
            if val in temp and check[idx] == 0:
                check[idx] = 1
                queue.append((val, c+1))


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
