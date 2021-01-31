from itertools import combinations
def solution(relation):
    answer = []
    cols = len(relation[0])
    rows = len(relation)
    arr = [i for i in range(cols)]

    for i in range(1, cols+1):
        com = list(combinations(arr, i)) # i 자리수 조합
        for tup in com: # 조합 돌려보기 
            tup = set(tup)
            if minimality(answer, tup) is False: # 최소성 검사
                continue
            a = set()
            for j in range(rows): #모든 행 방문
                ele = tuple(relation[j][nCol] for nCol in tup) # 튜플로 조합 열 번호값 가져오기
                a.add(ele) # set에 넣기
            if len(a) == rows: # set의 길이와 행의 크기와 같다면 유일성 적합
                answer.append(tup) # 조합 목록 추가

    return len(answer)

def minimality(answer, tup):
    for i in answer:
        if i.issubset(tup):
            return False
    return True