# 2레벨 2018 KAKAO BLIND RECRUITMENT      [3차] 파일명 정렬
# 정규표현식 이용하는 문제
# 이차원배열의 다중조건 정렬
import re


def solution(files):
    answer = []
    file = []
    p = re.compile(r"[ a-zA-Z.,-]+|[\d]{0,5}")
    for i in files:
        temp = p.findall(i)
        temp.append(i)
        print(temp)
        file.append(temp)

    file.sort(key=lambda x: (x[0].upper(), int(x[1])))
    answer = [i[-1] for i in file]

    return answer


"""
입출력
"""
# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files = ["img000012345", "img1.png", "img2,IMG02"]
# 정답 = [img000012345, img1.png, img2, IMG02]
print(solution(files))