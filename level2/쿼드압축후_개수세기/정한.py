# 월간 코드 챌린지 시즌1    쿼드압축 후 개수 세기
def quadtree_last_check(arr):
    one = sum(arr[0]) + sum(arr[1])
    zero = 4 - one
    if one == 4:
        return (0, 1)
    elif zero == 4:
        return (1, 0)
    else:
        return (zero, one)


def spliting_arr(side_len, arr):
    if side_len == 2:
        return quadtree_last_check(arr)

    target = [[0, 0], [0, side_len // 2], [side_len // 2, 0], [side_len // 2, side_len // 2]]
    check = ()
    result = [0, 0]
    zero_cnt, one_cnt = 0, 0

    for i in range(4):  # 4등분
        split_arr = [[0] * (side_len // 2) for _ in range(side_len // 2)]

        for j in range(0, side_len // 2):  # x 증가
            for q in range(0, side_len // 2):  # y 증가
                split_arr[j][q] = arr[target[i][0] + j][target[i][1] + q]

        one = sum(sum(split_arr, []))
        zero = (side_len // 2) ** 2 - one
        if zero == 0:  # zero가 0이니까 모두 1
            one_cnt += 1
            check = (0, 1)
        elif one == 0:  # one이 0이니까 모두 0
            zero_cnt += 1
            check = (1, 0)
        else:
            check = spliting_arr(side_len // 2, split_arr)  # 안합쳐지면 재귀

        result[0] += check[0]
        result[1] += check[1]

        # 4등분 한 모든 결과가 0, 1일경우 예외처리
        if zero_cnt == 4:
            result = [1, 0]
        elif one_cnt == 4:
            result = [0, 1]

    return tuple(result)


def solution(arr):
    side_len = len(arr[0])
    if side_len == 1:
        if arr[0][0] == 1:
            return [0, 1]
        else:
            return [1, 0]
    else:
        answer = list(spliting_arr(side_len, arr))
    return answer


"""
출력 예시
"""
arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
# arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# arr = [[1,1],[1,1]]
# arr = [[0, 0], [0, 0]]
# arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# arr = [[0]]
print(solution(arr))
