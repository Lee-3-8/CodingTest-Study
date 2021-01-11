def solution(s):
    answer = 0
    change = 0

    for i in range(1, (len(s)//2 + 2)): # 글자수가 1이었을때 안됨
        change = stringSlice(s,i)
        if i == 1 or answer > change:
            answer = change
    return answer

def stringSlice(string, n) :
    index = 0
    result = ''
    while(index < len(string)):
        compare = string[index:index+n]
        count = 0
        while(compare == string[index:index+n]):
            count += 1
            index += n
        if count > 1 :
            result = result + str(count) + compare
        else :
            result = result + compare
    return len(result)

print(solution("a"))