from itertools import combinations

def solution(relation):
    answer = 0
    input_len = len(relation[0])
    candi_column = list(range(input_len))
    temp_candi = {}
    for c in candi_column:
        temp_candi[c] = set()

    for i in relation:
        for c in candi_column:
            temp_candi[c].add(i[c])
    
    for c in candi_column:
        if len(temp_candi[c]) != len(relation):
            answer += 1
            candi_column.remove(c)

    candi_column2 = list(combinations(candi_column,2))

    for c in candi_column2:
        temp_candi[c] = set()
    
    for i in relation:
        for c in candi_column2:
            string_sum = ''
            for k in c:
                string_sum += i[k]
            temp_candi[c].add(string_sum)  

    for c in candi_column2:
        if len(temp_candi[c]) != len(relation):
            answer += 1
            candi_column2.remove(c)          

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

def test():
    a = [[1,2],[3,4]]
    print(1 in a)
test()