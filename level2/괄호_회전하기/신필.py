
def solution(s):
    open_tag = ['(','[','{']
    tagMap = {
        '(':')',
        '[':']',
        '{':'}'
    }
    def is_right_tags(tags):
        que = []
        for tag in tags:
            if que and tagMap[que[-1]] == tag:
                que.pop()
            elif tag in open_tag:
                que.append(tag)
            else: return False
        return False if que else True
        
    rotate_tags = [is_right_tags(s[i:]+s[:i]) for i in range(len(s))]
    return sum(rotate_tags)

if __name__ == '__main__':
    print(solution(	"}]()[{"))