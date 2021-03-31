from collections import deque

def solution(people, limit, answer=0):
    people = deque(sorted(people))
    while people:
        bag = 0
        while people and bag + people[-1] <= limit:
            bag += people.pop()
        while people and bag + people[0] <= limit:
            bag += people.popleft()
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))