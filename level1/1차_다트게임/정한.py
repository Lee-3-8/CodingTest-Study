# 2018 KAKAO BLIND RECRUITMENT  [1차] 다트 게임


def solution(dartResult):
    answer = 0

    cal_list = []

    for i, char in enumerate(dartResult):
        # 보너스
        if char == "S":
            cal_list[len(cal_list) - 1] **= 1

        elif char == "D":
            cal_list[len(cal_list) - 1] **= 2

        elif char == "T":
            cal_list[len(cal_list) - 1] **= 3

        # 옵션
        elif char == "#":
            cal_list[len(cal_list) - 1] = -cal_list[len(cal_list) - 1]

        elif char == "*":
            cal_list[len(cal_list) - 1] = cal_list[len(cal_list) - 1] * 2

            if len(cal_list) >= 2:
                cal_list[len(cal_list) - 2] = cal_list[len(cal_list) - 2] * 2

        # 숫자 추가 (총 3회)
        else:
            if len(cal_list) > 0 and dartResult[i - 1].isdecimal() and char == "0":
                cal_list[len(cal_list) - 1] *= 10

            else:
                cal_list.append(int(char))

    answer = sum(cal_list)
    return answer


# dartResult = "1S2D*3T"
# dartResult = "1D2S#10S"
# dartResult = "1D2S0T"
# dartResult = "1S*2T*3S"
# dartResult = "1D#2S*3S"
# dartResult = "1T2D3D#"
# dartResult = "1D2S3T*"

print(solution(dartResult))