import re
def solution(expression):
    nums = re.findall(r"\d+", expression)
    operand = re.findall(r"\D", expression)

    order = list(set(operand))
    S = operation(nums, operand, order) # 길이가 1일때 예외처리
    lenOrder = len(order)

    for i in range(lenOrder):
        order[0], order[i] = order[i], order[0]
        for _ in range(lenOrder - 1):
            order[lenOrder-2], order[lenOrder-1] = order[lenOrder-1], order[lenOrder-2]
            S = max(S, operation(nums, operand, order))
    
    return S



def operation(Nums, Operand, Order):
    nums = Nums[:]
    operand = Operand[:]
    order = Order[:]

    for i in order:
        j = 0
        while(j < len(operand)):
            if operand[j] == i:
                if i == '*':
                    result = int(nums[j]) * int(nums[j+1])
                elif i == '+':
                    result = int(nums[j]) + int(nums[j+1])
                elif i == '-':
                    result = int(nums[j]) - int(nums[j+1])
                nums.pop(j+1)
                nums[j] = str(result)
                operand.pop(j)
                j -= 1
            j += 1
    return abs(int(nums[0]))