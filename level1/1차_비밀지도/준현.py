n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

answer = ""
answer_list = []
arr1 = list(map(lambda x: (bin(x)[2:]), arr1))
arr1 = list(map(lambda x: x.zfill(n), arr1))
arr2 = list(map(lambda x: (bin(x)[2:]), arr2))
arr2 = list(map(lambda x: x.zfill(n), arr2))
for idx, val in enumerate(arr1):
    for jdx, jval in enumerate(val):
        if jval == '0' and arr2[idx][jdx] == '0':
            answer += " "
        else:
            answer += "#"
    answer_list += [answer]
    answer = ""

print(answer_list)
