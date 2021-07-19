from itertools import permutations
import re


def isMatch(user_id, ban_id):
    for i in range(len(ban_id)):
        p = re.compile(ban_id[i])
        if not p.match(user_id[i]) or len(user_id[i]) != len(ban_id[i]):
            return False
    return True


def solution(user_id, banned_id):
    ban_id = []
    answer = []
    for i in banned_id:
        b = i.replace('*', '.')
        ban_id.append(b)
    for i in permutations(user_id, len(ban_id)):
        if isMatch(i, ban_id):
            i = set(i)
            if i not in answer:
                answer.append(i)
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned_id = ["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))
