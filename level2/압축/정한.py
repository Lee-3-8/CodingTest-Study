# 2018 KAKAO BLIND RECRUITMENT      [3차] 압축
# chr, ord 을 이용해 아스키 코드 이용
# 뇌절 파티한 문제 (꼭 다시 풀자)


def solution(msg):
    answer = []
    indexing = dict()
    idx = 26
    max_len = 1
    for i in range(0, idx):
        indexing[i + 1] = f"{chr(ord('A')+i)}"

    i = 0
    while i < len(msg):
        attach = ""
        for j in range(max_len, 0, -1):
            for key, value in indexing.items():
                if msg[i : i + j] == value:
                    answer.append(key)
                    if i + j < len(msg):
                        attach = msg[i + j]
                    else:
                        return answer
                    break
            if attach != "":
                break

        idx += 1
        indexing[idx] = f"{indexing[answer[-1]]+attach}"

        i += len(indexing[idx]) - 1
        if max_len < len(indexing[idx]):
            max_len = len(indexing[idx])

    return answer


# msg = "KAKAO"
# msg = "TOBEORNOTTOBEORTOBEORNOT"
msg = "ABABABABABABABAB"
print(solution(msg))
# 기댓값 [11, 1, 27, 15]


# 알파벳
# print(f"{chr(ord('a')+1)}")