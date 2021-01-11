def cacl_split(split_len , str):
    result = []
    cnt = 0
    str_cnt = 0
    split = [str[i:i+split_len] for i in range(0, len(str),split_len)]
    while cnt<len(split):
        if split(cnt) == split(cnt + 1):
            str_cnt += 1
            cnt += 1
        else:
            result += (str(str_cnt) + split(cnt))
            cnt += 1


    return len(result)

def solution(s):
    answer = None
    for i in range(len(s)):
        answer.append(cacl_split(i,s))
    return min(answer)