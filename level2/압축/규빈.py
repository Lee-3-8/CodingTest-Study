from collections import deque
def solution(msg):
    answer = []
    msg = deque(msg)
    
    dic = { chr(ord('A') + i) : i+1 for i in range(26) }

    while(msg):
        w = msg.popleft()

        for _ in range(len(msg)):
            if w + msg[0] not in dic:
                dic[w + msg[0]] = len(dic)+1
                answer.append(dic[w])
                break
            w += msg.popleft()
        
        if not msg:
            answer.append(dic[w])

    return answer