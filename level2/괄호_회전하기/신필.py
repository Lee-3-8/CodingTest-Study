
def solution(s):
    tagMap = {
        '(':')',
        '[':']',
        '{':'}'
    }
    def is_right_tags(tags):
        stack = []
        for tag in tags:
            if stack and tagMap[stack[-1]] == tag: stack.pop()
            elif tag in tagMap: stack.append(tag)
            else: return False
        return False if stack else True
        
    rotate_tags = [is_right_tags(s[i:]+s[:i]) for i in range(len(s))]
    return sum(rotate_tags)

if __name__ == '__main__':
    print(solution(	"}]()[{"))