import re
from itertools import product
def solution(user_id, banned_id):
    answer = set()

    arr = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        for name in user_id:
            newID = banned_id[i].replace('*', '.')
            result = re.match(newID, name)
            if result and len(result.group()) == len(name):
                arr[i].append(name)

    for users in product(*arr):
        s_user = set(users)
        if len(s_user) == len(users):
            answer.add(tuple(sorted(list(users))))

    return len(answer)