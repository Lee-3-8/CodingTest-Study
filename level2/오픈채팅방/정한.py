# 2레벨     2019 KAKAO BLIND RECRUITMENT    오픈채팅방
# 2레벨치고는 난이도가 낮은 문제
# 문자열 split 사용


def solution(record):
    user = {}
    list_re = []
    for info in record:
        temp = info.split(" ")

        if temp[0] == "Enter" or temp[0] == "Change":
            user[f"{temp[1]}"] = temp[2]

        if temp[0] != "Change":
            list_re.append(temp)

    for idx, info in enumerate(list_re):
        trans = f"{user[info[1]]}님이 "
        if info[0] == "Enter":
            trans = trans + "들어왔습니다."
        else:
            trans = trans + "나갔습니다."

        list_re[idx] = trans

    return list_re


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]
print(solution(record))
