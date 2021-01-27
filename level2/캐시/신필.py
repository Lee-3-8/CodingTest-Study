from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    answer = deque(maxlen=cacheSize) # 최대값 지정하면 앞에서 부터 자동삭제
    time = 0
    for v in cities:
        v = v.lower()
        if v in answer:
            answer.remove(v) # 두번 돌긴함 for문을 하나더 쓰기 싫엇음
            time -= 4 # 어차피 마지막에 5를 더하니까 1더하는게 아니라 -4를 함 코드 줄이려고 이렇게함
        answer.append(v) # 뒤로 넣음 
        time += 5
        print(time,answer)
    return time

# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"]))
