import re
from itertools import permutations
from copy import deepcopy

def solution(expression):
    find_flag = list(permutations(set(re.compile(r"[-*+]").findall(expression))))
    result = re.compile(r"[\d]+|[-*+]").findall(expression)
    k = 0
    calc_result = []
    for i in find_flag:
        print(i)
        temp = deepcopy(result)
        print(temp)
        for v in i:
            print(v)
            k = 0
            while k < len(temp):
                if temp[k] == v:
                    temp[k] = str(eval(temp[k-1]+temp[k]+temp[k+1]))
                    del temp[k+1]
                    del temp[k-1]
                else :
                    k+=1
                print(temp)
        calc_result.append(temp)

    print(calc_result)
    calc_result = sum(calc_result,[])
    calc_result = list(map(lambda x: abs(int(x)),calc_result))
    print(calc_result)
    return max(calc_result)

# print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))