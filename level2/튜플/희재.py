import re

def solution(s):
    set_list = re.compile("{[\d,]+}").findall(s)
    set_list = sorted([list(eval(i)) for i in set_list])
    set_list.sort(key=lambda x: len(x))
    answer = {i:None for i in sum(set_list, [])}
    return list(answer.keys())

if __name__ == '__main__':
    result = solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
    print(result)