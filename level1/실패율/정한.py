# 2019 KAKAO BLIND RECRUITMENT 실패율


def solution(N, stages):
    answer = []
    result = dict()
    all_people = len(stages)

    for i in range(1, N + 1):
        result[i] = {"fail": 0, "fail_cnt": 0}

    # 해당 스테이지 클리어 횟수, 실패 횟수(도달)저장
    for num in stages:
        if N + 1 == num:
            continue

        result[num]["fail_cnt"] += 1

    # 실패율 저장
    for i in range(1, N + 1):
        if all_people == 0:
            break

        if result[i]["fail_cnt"] == 0:
            result[i]["fail"] = 0

        else:
            result[i]["fail"] = result[i]["fail_cnt"] / all_people

        all_people -= result[i]["fail_cnt"]

    answer = sorted(result.items(), key=lambda x: -x[1]["fail"])
    print(answer)
    answer = [i[0] for i in answer]

    return answer


"""
출력 확인
"""
# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

N = 4
stages = [4, 4, 4, 4, 4]


print(solution(N, stages))