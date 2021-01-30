def solution(record):
    entry_dict = {"Enter":"님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    answer, nick_dict = [], {}

    for log in [i for i in record if not i.startswith('Leave')]:
        uid, nick = log.split()[1:]
        nick_dict[uid] = nick

    for log in [i for i in record if not i.startswith('Change')]:
        entry, uid = log.split()[:2]
        answer.append(nick_dict[uid] + entry_dict[entry])

    return answer

if __name__ == '__main__':
    print(solution(	["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))