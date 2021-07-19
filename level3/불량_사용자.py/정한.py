# 2019 카카오 개발자 겨울 인턴십    불량 사용자
from itertools import product, combinations


def solution(user_id, banned_id):
    avilable = [[] for _ in range(len(banned_id))]
    user_id_len = len(user_id)
    banned_id_len = len(banned_id)
    for idx_b, ban in enumerate(banned_id):
        ban_len = len(ban)
        for idx, user in enumerate(user_id):
            if len(user) == ban_len:
                flag = 1
                for u, b in zip(user, ban):
                    if b != "*" and u != b:
                        flag = 0
                        break
                if flag:
                    avilable[idx_b].append(idx)

    set_li = set()
    for item in product(*avilable):
        item = set(item)
        if len(item) == banned_id_len:
            set_li.add(tuple(item))

    return len(set_li)


if __name__ == "__main__":
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
    print(
        solution(
            ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]
        )
    )
