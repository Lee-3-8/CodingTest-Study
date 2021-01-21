def solution(n, words):
    last = words[0][0] # 처음껄 그냥 넣음 
    for i,v in enumerate(words):
        if v[0] != last or v in words[:i]:
            return [(i%n) + 1, (i//n) +1]
        last = v[-1]
    return [0,0]
# print(solution())
# words를 다돌려서 틀린것에 해당하는 조건을 찾아서 그 때의 사람을 계산 