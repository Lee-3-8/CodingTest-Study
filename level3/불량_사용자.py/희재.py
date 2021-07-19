import re
from itertools import product

def solution(user_id, banned_id):
    patterns = [re.compile("^%s$" % i.replace("*", ".")) for i in banned_id]
    patterns_len = len(patterns)
    matched = [[] for _ in range(patterns_len)]
    for u_idx in range(len(user_id)):
        for p_idx in range(patterns_len):
            if patterns[p_idx].match(user_id[u_idx]):
                matched[p_idx].append(u_idx)
    answer = []
    for prod in product(*matched):
        prod_set = set(prod)
        if len(prod_set) == patterns_len and prod_set not in answer:
            answer.append(prod_set)
    return len(answer)


if __name__ == '__main__':
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "abc1**"]
    ))
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["*rodo", "*rodo", "******"]
    ))
    print(solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"]
    ))