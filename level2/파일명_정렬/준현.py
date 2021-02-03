
files = ["img000012345", "img1.png", "img2", "IMG02"]
a = [1, 2]

print(a[0:1])


def solution(files):
    answer = []
    for i in files:
        temp = []
        head = ''
        number = ''
        tail = ''
        for idx in range(len(i)):
            if i[idx].isdigit():
                head += i[:idx].upper()
                cnt = 0
                for jdx in range(idx, len(i)):
                    if cnt >= 5:
                        number = (int(i[idx:idx+5]))
                        tail += i[idx+5:]
                        break
                    if i[jdx].isdigit():
                        cnt += 1
                    else:
                        number = int(i[idx:idx+cnt])
                        tail += i[idx+cnt:]
                        break
                number = int(i[idx:idx+cnt])
                break
        temp.append(head)
        temp.append(number)
        temp.append(tail)
        temp.append(i)
        answer.append(temp)
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    answer = [x[3] for x in answer]
    return answer


print(solution(files))
