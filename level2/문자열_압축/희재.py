def encode(s, n, origin_len):
    s_list = [s[i:i+n] for i in range(0, len(s), n)] + [""]
    cur_len = 1
    
    for i in range(1, len(s_list)):
        if s_list[i] == s_list[i-1]: 
            cur_len += 1
            origin_len -= len(s_list[i])
        elif cur_len > 1:
            origin_len += len(str(cur_len))
            cur_len = 1
    
    return origin_len

def solution(s):
    origin_len = len(s)
    answer = origin_len
    
    for i in range(1, answer // 2 + 1):
      enc_len = encode(s, i, origin_len)
      answer = min(answer, enc_len)   
    return answer


if __name__ == '__main__':
    result = solution("bbaabaaaabb")
    print(result)