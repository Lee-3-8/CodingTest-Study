def solution(record):
    uid_map = {}
    action_map = {
        'Enter' : "들어왔습니다.",
        'Leave' : "나갔습니다."
    }
    result = []
    for v in record:
        command = v.split(' ')
        if command[0] != 'Leave':
            uid_map[command[1]] = command[2]
            print(command[0], uid_map)
    for v in record:
        command = v.split(' ')
        if command[0] != 'Change':
            result.append(f"{uid_map[command[1]]}님이 {action_map[command[0]]}")

    return result

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

# def test():
#     a = 1
#     b = 'f"{a} 입니다"'
#     print(eval(b))
#     a = 2
#     print(eval(b))

# test()
