def solution(record):
    answer = []
    user = {}
    verb = {'Enter' : '님이 들어왔습니다.',
            'Leave' : '님이 나갔습니다.'}
    for string in record:
        strSplit = string.split()
        if len(strSplit) == 3:
            user[strSplit[1]] = strSplit[2]

    for string in record:
        strSplit = string.split()
        if strSplit[0] != 'Change':
            s = user[strSplit[1]] + verb[strSplit[0]]
            answer.append(s)
            
    return answer