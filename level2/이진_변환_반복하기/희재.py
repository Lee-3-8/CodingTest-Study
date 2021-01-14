def solution(s):
    proc_cnt, zero_cnt = 0, 0
    while s != "1":
        new_len = s.count('1')
        zero_cnt += len(s) - new_len
        s = bin(new_len)[2:]
        proc_cnt += 1
    return [proc_cnt, zero_cnt]


if __name__ == '__main__':
    result = solution("110010101001")
    print(result)