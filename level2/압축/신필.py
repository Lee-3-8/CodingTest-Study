import string
from collections import deque 

def solution(msg):
    len_dic = 26
    str_dic = { key:val+1 for val,key in enumerate(string.ascii_uppercase)}
    result = []
    print(str_dic)
    i,j = 1,0
    while i <= len(msg):
        compare = msg[j:i]
        print(compare , j ,i ,str_dic ,msg )
        if compare not in str_dic:
            result.append(str_dic[msg[j:i-1]])
            len_dic += 1
            str_dic[compare] = len_dic
            j = i-1
        else:
            i+=1
    result.append(str_dic[msg[j:i-1]])
    

    return result

# print(solution('KAKAO'))
# print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))

# def test():
#     ab = 'abc'
#     print(ab[:1])

# test()