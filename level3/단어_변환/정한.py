# 3레벨     코딩테스트 고득점 Kit     단어 변환
# bfs 사용
from collections import deque

answer = 0


def solution(begin, target, words):
    def check(now, compare):
        cnt = 0
        for n, c in zip(now, compare):
            if n != c:
                cnt += 1
        return 1 if cnt == 1 else 0

    def bfs():
        global answer
        if answer != 0 or not deque:
            return answer

        now = deq.popleft()
        for word in words:
            if check(now[0], word):
                if word == target:
                    answer = now[1] + 1
                deq.append([word, now[1] + 1])

        return bfs()

    deq = deque()
    deq.append([begin, 0])
    return bfs() if target in words else 0


if __name__ == "__main__":
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
