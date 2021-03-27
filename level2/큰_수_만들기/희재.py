def solution(number, k):
    number = list(number)
    answer = ''
    max_idx = -1
    for i in range(1, len(number) - k + 1):
        max_num = "0"
        for i in range(max_idx + 1, k + i):
            if number[i] == '9':
                max_num, max_idx = number[i], i
                break
            if number[i] > max_num:
                max_num, max_idx = number[i], i
        answer += max_num
    return answer

if __name__ == '__main__':
    print(solution("32323233232", 1))


"""
def solution(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])
"""