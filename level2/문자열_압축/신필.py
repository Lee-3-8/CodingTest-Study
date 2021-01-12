def cacl_split(split_len , input):
    result = []
    temp, cnt, cur_len = '', 1, len(input)-1
    # split = [input[i:i+split_len] for i in range(0, len(input),split_len)]
    # print(split)
    for i in range(0, len(input),split_len):
        if temp == input[i:i+split_len]:
            cnt += 1
        else:
            if cnt >= 2:
                cur_len -= (cnt*split_len - split_len -len(str(cnt)) )
            cnt = 1
        temp = input[i:i+split_len]
        print(temp , cnt , cur_len)
    return cur_len

def solution(s):
    answer = []
    if len(s) == 1 : return 1
    for i in range(1, len(s) //2 + 1 ):
        answer.append(cacl_split(i,s+' '))
    print(answer)
    return min(answer)

solution("xxxxxxxxxxyyy")