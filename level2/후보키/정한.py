# 2레벨     2019 KAKAO BLIND RECRUITMENT    후보키
from itertools import combinations


def solution(relation):
    key_list = []
    idx = [i for i in range(len(relation[0]))]  # 인덱스 번호

    for i in range(1, len(relation[0]) + 1):
        idx_com = combinations(idx, i)
        # print(list(idx_com)) # 왜이거찍고하면 오류나지??? list()하고나면 초기화됨;;
        check_key(key_list, idx_com, relation)

    print("key_list: ", key_list)
    return len(key_list)


def check_key(key_list, idx_com, relation):

    for i in idx_com:  # i 는 키후보 컬럼 튜플
        temp = []
        for q in relation:
            t = []
            for j in i:
                t.append(q[j])
            temp.append(tuple(t))

        if len(temp) == len(set(temp)) and check_min(key_list, i):
            key_list.append(i)


def check_min(key_list, target):
    flag = 1
    for i in key_list:  # key_list에 있는 키(튜플)
        for j in i:
            if j in target:
                flag = 0
            else:
                flag = 1  # 해당키에 최소성 충족
                break
        if flag == 0:  # 해당키에 최소성 미통
            return 0
    return 1


# relation = [
#     ["100", "ryan", "music", "2"],
#     ["200", "apeach", "math", "2"],
#     ["300", "tube", "computer", "3"],
#     ["400", "con", "computer", "4"],
#     ["500", "muzi", "music", "3"],
#     ["600", "apeach", "music", "2"],
# ]
# 2

# relation = [
#     ["a", "b", "c"],
#     ["1", "b", "c"],
#     ["a", "b", "4"],
#     ["a", "5", "c"],
# ]
# 1

relation = [
    ["a", "1", "4"],
    ["2", "1", "5"],
    ["a", "2", "4"],
]
# 2
print(solution(relation))
