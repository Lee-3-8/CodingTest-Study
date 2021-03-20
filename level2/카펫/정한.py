# 2레벨     코딩테스트 고득점 Kit     카펫
def solution(b, y):
    for i in range(1, y+1):
        if y % i == 0:
            if b == 4 + i * 2 + y // i * 2:
                return [y // i + 2, i + 2]


if __name__ == "__main__":
    print(solution(8, 1))
