# 2020 KAKAO BLIND RECRUITMENT  문자열 압축


def solution(s):
    s_len = len(s)
    answer = s_len
    before_cnt = 0
    before_ch = ""

    for i in range(1, s_len // 2 + 1):
        ch_list, cnt_list, result_len = [], [], 0

        for j in range(0, s_len // i + 1):
            if (j + 1) * i > s_len:
                ch = s[j * i :]
            else:
                ch = s[j * i : (j + 1) * i]

            if j != 0 and ch == before_ch:
                cnt_list[before_cnt] += 1

            else:
                ch_list.append(ch)
                cnt_list.append(1)
                before_cnt = len(cnt_list) - 1

            before_ch = ch

        print(ch_list)
        print(cnt_list)
        # 총 길이 (숫자의 자릿수 유의)
        for i in range(len(ch_list)):
            if cnt_list[i] != 1:
                result_len += len(str(cnt_list[i]))

            result_len += len(ch_list[i])

        if result_len < answer:
            answer = result_len

    return answer


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
# s = "a"*100 + "b"
# s="xxxxxxxxxxyyy"
s = "bbaabaaaab"
print(solution(s))