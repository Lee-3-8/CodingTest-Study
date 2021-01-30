from itertools import combinations

def is_minimal(answers, comb):
    for answer in answers:
        if not (answer - comb):
            return False
    return True

def is_unique(relation, comb):
    data_list = [tuple([row[i] for i in comb]) for row in relation]
    return len(set(data_list)) == len(data_list)

def solution(relation):
    answers = []
    for i in range(1, len(relation[0]) + 1):
        for comb in combinations(range(len(relation[0])), i):
            if is_minimal(answers, set(comb)) and is_unique(relation, comb):
                answers.append(set(comb))
    return len(answers)

if __name__ == '__main__':
    # print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
    print(solution([["a","1","4"],
                    ["2","1","5"],
                    ["a","2","4"],]))