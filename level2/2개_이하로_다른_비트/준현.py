
def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            binary = '0'+str(bin(i)[2:])
            zero = list(filter(lambda x: binary[x] == '0', range(len(binary))))
            binary = binary[:zero[-1]]+'10'+binary[zero[-1]+2:]
            answer.append(int('0b'+binary, 2))
    return answer


numbers = [2, 7, 9]
print(solution(numbers))
# 1=2
# 2=3
# ---
# 3=5
# 4=5
# 5=6
# 6=7
# ---
# # 2^3-1 = 2^3+2^1+1
# 7=11
# 8=9

# # 2^4 -1= 2^5+2^2+2
# 15=
