record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    answer = []
    order_list = []
    people_list = {}
    for i in record:
        temp = i.split()
        if temp[0] == "Change":
            people_list[temp[1]] = temp[2]
        else:
            if temp[0] == "Enter":
                people_list[temp[1]] = temp[2]
            order_list.append((temp[0], temp[1]))

    for j in order_list:
        if j[0] == "Enter":
            answer.append("{0}님이 들어왔습니다.".format(people_list[j[1]]))
        else:
            answer.append("{0}님이 나갔습니다.".format(people_list[j[1]]))
    return answer


print(solution(record))
