
def calc_n(num,jinsu):
    transfer = '0123456789ABCDEF'
    m,n = divmod(num,jinsu)
    if m == 0:
        return transfer[n]
    else:
        return calc_n(m , jinsu) + transfer[n]

def solution(n, t, m, p):
    numbers = ''
    result = ''
    for i in range(t*m):
        numbers += calc_n(i,n)
        print(numbers)
    for i in range(t*m):
        if i%m == p-1:
            result += numbers[i]
        print(i,numbers[i],result)
    return result

print(solution(2,4,2,1))
# print(solution(16,16,2,1))
# print(solution(16,16,2,2))
