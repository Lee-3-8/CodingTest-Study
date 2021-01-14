# 월간 코드 챌린지 시즌1    이진 변환 반복하기
# 진수 변환 사용 문제
# 문자열에서 특정 문자 삭제


def solution(s):
    answer = [0, 0]

    while int(s) != 1:
        a_len = len(s)
        s = s.replace("0", "")  # "0" 문자 삭제
        answer[1] += a_len - len(s)

        s = str(format(len(s), "b"))
        answer[0] += 1

    return answer


# s = "110010101001"
# s= "01110"
s = "1111111"
print(solution(s))