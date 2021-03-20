# 1레벨     코딩테스트 고득점 Kit     모의고사
def solution(answers):
    answer = []
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p1 = len(people1)
    p2 = len(people2)
    p3 = len(people3)
    result = [0, 0, 0]
    for i in range(len(answers)):
        if people1[i % p1] == answers[i]:
            result[0] += 1

        if people2[i % p2] == answers[i]:
            result[1] += 1

        if people3[i % p3] == answers[i]:
            result[2] += 1

    cutline = max(result)

    for i in range(3):
        if result[i] == cutline:
            answer.append(i + 1)
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5]))