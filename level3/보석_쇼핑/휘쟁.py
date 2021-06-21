from collections import deque, defaultdict

def solution(gems):
    all_gems, cur_set = set(gems), set()
    counter, left, right = defaultdict(int), 0, 0
    answer = [0, float('inf')]

    while right < len(gems):
        while right < len(gems) and len(cur_set) < len(all_gems):
            cur_set.add(gems[right])
            counter[gems[right]] += 1
            right += 1
        while len(cur_set) == len(all_gems):
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                cur_set.remove(gems[left])
            left += 1
        if answer[1] - answer[0] > right - left:
            answer = [left, right]

    return answer

if __name__ == '__main__':
    print(solution(
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    ))
    print(solution(
        [1,2,3,4,5,6]
    ))
    print(solution(
        ["AA", "AB", "AC", "AA", "AC"]
    ))