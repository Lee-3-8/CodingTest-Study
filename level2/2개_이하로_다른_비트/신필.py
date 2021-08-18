# python은 오른쪽부터 replace가 없는가?...
# 파이썬은 문자열의 인덱스만 변경이 불가능?
def func_x(num):
    if num %2 == 0: #맨 뒤 비트가 0 이면 걍+1
        return num+1
    else: 
        bin_num = format(num,'b')
        zero_index = bin_num.rfind('0')
        if zero_index == -1: # 2^n - 1 
            result = '0b'+ bin_num.replace('1','10',1)
        elif zero_index == len(bin_num) - 1: # 11100 -> 11101
            result = '0b'+bin_num[:zero_index] + '1'
        else:
            result = '0b'+bin_num[:zero_index] + '10' + bin_num[zero_index+2:]
        return int(result,2)

def solution(numbers):
    return list(map(func_x,numbers))

if __name__ == '__main__':
    print(solution([11, 64]))