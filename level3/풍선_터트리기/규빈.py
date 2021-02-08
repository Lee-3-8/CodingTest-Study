from itertools import permutations
def solution(a):
    answer = len(a)
    left, right = 0, answer - 1
    minL, minR = a[left], a[right]

    while(left != right):
        if minL > minR:
            left += 1
            if a[left] > minL:
                answer -= 1
            else:
                minL = a[left]
        else:
            right -= 1
            if a[right] > minR:
                answer -= 1
            else:
                minR = a[right]
    return answer