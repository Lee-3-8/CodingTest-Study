from collections import deque

def solution(enter, leave):
    answer = [0 for _ in range(len(enter))]
    enter, leave, room = deque(enter), deque(leave), set()
    while leave:
        cur_leave = leave.popleft()
        while cur_leave not in room:
            room.add(enter.popleft())
        room.remove(cur_leave)
        for room_i in room:
            answer[room_i - 1] += 1
        answer[cur_leave - 1] += len(room)
    return answer

if __name__ == '__main__':
    print(solution([1,3,2], [1,2,3]))
    print(solution([1,4,2,3], [2,1,3,4]))
    print(solution([3,2,1], [2,1,3]))
