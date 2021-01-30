import string

msg = "TOBEORNOTTOBEORTOBEORNOT"


def check_len(check_list, arr):
    end = 1
    while True:
        if end == len(check_list):
            return end-1
        elif check_list[:end] not in arr:
            return end-1
        else:
            end += 1


def solution(msg):
    answer = []
    msg += ' '
    arr = list(string.ascii_uppercase)
    i = 0
    while i < len(msg)-1:
        current_len = check_len(msg[i:], arr)
        print(current_len)
        if current_len <= 1:
            print("f", msg[i:i+1])
            answer.append(arr.index(msg[i:i+1])+1)
            arr.append(msg[i:i+2])
            i += 1
        else:
            if current_len == len(msg[i:]):
                answer.append(arr.index(msg[i:i+current_len])+1)
                arr.append(msg[i:i+current_len+1])
                print("t", arr.append(msg[i:i+current_len+1]))
            else:
                answer.append(arr.index(msg[i:i+current_len])+1)
                arr.append(msg[i:i+current_len+1])
                print("t", arr.append(msg[i:i+current_len+1]))
            i += current_len
    return answer


print(solution(msg))
