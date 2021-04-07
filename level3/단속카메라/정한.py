# 3레벨     코딩테스트 고득점 Kit     단속카메라
from sys import maxsize


def solution(routes):
    routes.sort(key=lambda x: (x[0], x[1]))
    m = -maxsize
    M = maxsize
    cnt = 0
    for s, e in routes:
        if M < s:
            cnt += 1
            m = s
            M = e
        else:
            if m < s:
                m = s
            if M > e:
                M = e

    cnt += 1
    return cnt


if __name__ == "__main__":
    print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))