def solution(s):
    sum_length = 0
    min_length = len(s)
    if len(s) == 1:
        return 1
    for length in range(1, len(s)//2+1):
        count = 1
        temp = s[:length]
        for i in range(length, len(s), length):
            if s[i:i+length] == temp:
                count += 1
            else:
                temp = s[i:i+length]
                if count != 1:
                    sum_length += len(str(count))+length
                else:
                    sum_length += length
                count = 1
        if count != 1:
            sum_length += len(str(count))+length
        else:
            sum_length += len(temp)
        if min_length > sum_length and sum_length != 0:
            min_length = sum_length
        sum_length = 0
    return min_length
