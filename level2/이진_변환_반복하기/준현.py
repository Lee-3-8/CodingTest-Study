def trans_bin(s):
    count_one = sum(int(i) for i in s)
    count_zero = len(s)-count_one
    trans_bin = format(count_one, 'b')
    return trans_bin, count_zero


def solution(s):
    count_recursive = 0
    count_eraser_zero = 0
    while s != "1":
        count_recursive += 1
        s, temp = trans_bin(s)
        count_eraser_zero += temp
    return [count_recursive, count_eraser_zero]
