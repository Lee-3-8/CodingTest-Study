# 5레벨     코딩테스트 고득점 Kit     방의 개수
# 대각선 지나면 +1인듯
# 점으로 들어가는 선이 이미 그려진거면 +1 아닌?
from collections import defaultdict


def solution(arrows):
    now = [0, 0]
    direction = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    visit_v = defaultdict(lambda: defaultdict(int))
    visit_v[0][0] = 1
    visit_e = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))

    state = 1
    result = 0
    for d in arrows:
        dx, dy = direction[d]
        x = now[0] + dx
        y = now[1] + dy

        if state == 1:
            if visit_v[now[0]][now[1]] == 1 and visit_e[now[0]][now[1]][x][y] == 0:
                result += 1
                state = 0
            elif (
                visit_v[x][now[1]] == visit_v[now[0]][y] == 1 and visit_e[now[0]][now[1]][x][y] == 0
            ):  # 대각 통과
                result += 1

        else:
            visit_v[now[0]][now[1]] = 0
            state = 1

        visit_v[x][y] = 1
        visit_e[now[0]][now[1]][x][y] = 1
        now[0] = x
        now[1] = y

    return result


if __name__ == "__main__":
    print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
