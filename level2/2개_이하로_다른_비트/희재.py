def solution(numbers):
    answer = []
    for i in numbers:
        bin_i = "0" + bin(i)[2:]
        idx = bin_i.rfind("0")
        conv_i = "1".join(bin_i.rsplit('0', 1))
        conv_i = conv_i[:idx + 1] +\
                 conv_i[idx+1:].replace('1', '0', 1)
        answer.append(int("0b" + conv_i, 2))
    return answer


if __name__ == '__main__':
    print(solution([2, 7]))