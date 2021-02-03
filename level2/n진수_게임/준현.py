import string


def convert(num=0, base=2):
    num_list = ['0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    division = num // base
    remain = num % base
    if division < base:
        return num_list[division] + num_list[remain]
    else:
        result = convert(division, base)

    return result + num_list[remain]

# def convert(n, base):
#     T = "0123456789ABCDEF"

#     q, r = divmod(n, base)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]


def solution(n, t, m, p):
    p -= 1
    answer = []
    for i in range(t*m):
        temp = convert(i, n)
        if temp[0] == '0':
            temp = temp[1:]
        answer += temp
    result = ''
    for i in range(0, t*m, m):
        result += answer[i+p]
    return result


print(solution(16, 16, 2, 2))
