# 2020 카카오 인턴십    수식 최대화
# 정규표현식과 순열을 이용하면 간단해지는 문제
import re
from itertools import permutations


def solution(expression):
    result = []
    list_math = re.findall(r"[\d]+|[^\d]+", expression)

    priority = list(permutations(["*", "+", "-"], 3))

    for i in priority:
        temp = list_math[:]
        for j in range(0, 3):
            idx = 0
            while len(temp) - 1 > idx:
                if temp[idx] == i[j]:
                    temp[idx - 1] = str(eval(temp[idx - 1] + temp[idx] + temp[idx + 1]))
                    del temp[idx]
                    del temp[idx]

                else:
                    idx += 1
        result.append(abs(int(temp[0])))

    print(result)
    return max(result)


# expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(solution(expression))