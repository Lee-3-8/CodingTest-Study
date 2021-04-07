# 3레벨     코딩테스트 고득점 Kit     N으로 표현
from collections import defaultdict


def solution(N, number):
    dic = defaultdict(set)
    dic[1] = set([N])
    dic[2] = set([10 * N + N, N // N, N + N, N * N, N - N])

    for i in range(1, 3):
        if number in dic[i]:
            return i

    count = 3
    while count:
        print(count)
        if count > 8:
            return -1

        dic[count].add(int(str(N) * count))
        for r in range(1, count // 2 + 1):
            for i in dic[r]:
                for j in dic[count - r]:
                    dic[count].add(i - j)
                    dic[count].add(j - i)
                    dic[count].add(i * j)
                    dic[count].add(i + j)
                    if j != 0:
                        dic[count].add(i // j)
                    if i != 0:
                        dic[count].add(j // i)
        if number in dic[count]:
            return count
        else:
            count += 1


if __name__ == "__main__":
    print(solution(5, 5))
