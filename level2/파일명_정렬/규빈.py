import re
def solution(files):
    answer = []
    sliced = []

    for i in files:
        head, number, tail = re.match(r'(\D+)(\d{1,5})(.*)', i).groups()
        sliced.append([head, number, tail])
    
    temp = sorted(sliced, key= lambda x : (x[0].lower(), int(x[1])))
    
    for i in temp:
        for j in files:
            head, number, tail = re.match(r'(\D+)(\d{1,5})(.*)', j).groups()
            if i == [head, number, tail]:
                answer.append(j)

    return answer