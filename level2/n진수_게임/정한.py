# 2018 KAKAO BLIND RECRUITMENT      [3차] n진수 게임
def solution(n, t, m, p):
    answer = ""
    result = ""
    convert = {
        2: "b",
        8: "o",
        10: "d",
        16: "x",
    }
    i = 0
    num = 0
    while len(result) < m * (t + 1):
        temp = format(num, convert[n])
        result += str(temp)
        num += 1

    for i in range(t):
        answer += result[i * m + p - 1].upper()

    return answer


# n, t, m, p = 2, 4, 2, 1
# 기댓값 〉	"0111"
n, t, m, p = 16, 16, 2, 1
# 기댓값 〉	"02468ACE11111111"
# print(solution(n, t, m, p))

print(format(15, "x"))
