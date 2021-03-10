

def solution(priorities, location):
    ln = len(priorities)
    seat = [0]*ln
    count = 1
    j = 0
    while count != ln+1:
        pr_max = max(priorities)
        while True:
            if j == ln:
                j %= ln
            if priorities[j] == pr_max:
                seat[j] = count
                count += 1
                priorities[j] = -float('inf')
                j += 1
                break
            j += 1
    return seat[location]


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
