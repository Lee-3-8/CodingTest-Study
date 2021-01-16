def operate(a, b, c):
    if c == '*':
        return a*b
    elif c == '-':
        return a-b
    else:
        return a+b


def solution(expression):
    number_list = []
    operate_list = []
    index = 0
    for idx, val in enumerate(expression):
        if idx == len(expression)-1:
            number_list += [int(expression[index:idx+1])]
        if val == '*' or val == '-' or val == '+':
            operate_list += val
            number_list += [int(expression[index:idx])]
            index = idx+1
    priority_operate = [['*', '-', '+'], ['*', '+', '-'], ['-', '*', '+'], ['-', '+', '*'],
                        ['+', '*', '-'], ['+', '-', '*']]

    answer = 0
    for i in range(len(priority_operate)):
        operate_ex = operate_list.copy()
        number_ex = number_list.copy()
        k = 0
        idx = 0
        while operate_ex:
            if priority_operate[i][k] == operate_ex[idx]:
                add = operate(number_ex[idx],
                              number_ex[idx+1], operate_ex[idx])
                number_ex[idx] = add
                del number_ex[idx+1]
                del operate_ex[idx]
            else:
                idx += 1
            if idx == len(operate_ex):
                idx = 0
                k += 1
        if answer < abs(number_ex[0]):
            answer = abs(number_ex[0])
    return answer
