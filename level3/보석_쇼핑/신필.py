def solution(gems):
    category = set(gems)
    category = len(category)
    temp = set()
    answer = (0,len(gems))
    for i in range(len(gems)):
        for j in range(i,len(gems)):
            temp.add(gems[j])
            if category == len(temp):
                answer = (i,j) if j-i < answer[1] - answer[0] else answer
                break
        temp.clear()
    return answer[0] + 1,answer[1]+1

if __name__ == '__main__':
    print(solution(	["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
    # print(solution(	["AA", "AB", "AC", "AA", "AC"]))