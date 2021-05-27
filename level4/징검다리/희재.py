def solution(dist, rocks, n):
    rocks = sorted(rocks) + [dist]

    def validate(limit):
        removed, start = 0, 0
        for r in rocks:
            if r - start > limit:
                start = r
            else:
                removed += 1
        return removed > n

    def search(left, right):
        mid = (left + right) // 2
        if left >= right:
            return left
        elif validate(mid):
            return search(left, mid - 1)
        else:
            return search(mid + 1, right)

    return search(0, dist)

if __name__ == '__main__':
    print(solution(
        25, [2, 14, 11, 21, 17], 2
    ))


"""
  2 11 14 17 21
 2 9  3  3  4  4
 
1 - 25 (12) >> 
"""
