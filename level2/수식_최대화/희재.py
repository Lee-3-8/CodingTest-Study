import re
from itertools import permutations

def calculate(expression, perm):
    for op in perm:
        pattern = re.compile(r"(\d+|\(-?\d+\))+[%s](\d+|\(-?\d+\))" % op)
        while True:
            formula = pattern.search(expression)
            if formula is None: break
            result = "(" + str(eval(formula.group())) + ")"
            expression = expression.replace(formula.group(), str(result))

    return abs(eval(expression))

def solution(expression):
    answer = float('-inf')
    op_set = set(re.compile(r"[*+-]").findall(expression))

    for perm in permutations(op_set):
        result = calculate(expression, perm)
        if result > answer:
            answer = result

    return answer

if __name__ == '__main__':
    result = solution("50*6-3*2")
    print(result)