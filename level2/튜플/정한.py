# 2019 카카오 개발자 겨울 인턴십    튜플
# 정규표현식 연습하기 좋은 문제
import re


def solution(s):
    answer = []

    temp = re.findall(r"{[\d|,]+}", s)  # { (숫자와 콤마만있는) }들 찾기
    temp.sort(key=lambda x: len(x))  # {}안 개수오름차순으로 정렬

    temp = " ".join(temp)  # 문자열하나로 합치기

    temp = re.findall(r"[\d]+", temp)

    for num_ch in temp:
        num = int(num_ch)
        if num not in answer:
            answer.append(num)

    return answer


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = "{{20,111},{111}}"
print(solution(s))


# re.findall(r"[\w']+", s)  [] 안에 작음따옴표 하나는 무엇?