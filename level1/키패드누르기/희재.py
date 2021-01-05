def init_board():
    board = [(3,1)]
    for i in range(3):
        for j in range(3):
            board += [(i, j)]
    return board


def get_dist(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])


def get_next_hand(cur, target_cur, hand):
    left_dist = get_dist(cur['L'], target_cur)
    right_dist = get_dist(cur['R'], target_cur)
    if left_dist < right_dist:
        return 'L'
    elif left_dist > right_dist:
        return 'R'
    else:
        if hand == 'left':
            return 'L'
        else:
            return 'R'


def solution(numbers, hand):
    LEFT_SIDE = set([1, 4, 7])
    RIGHT_SIDE = set([3, 6, 9])
    board = init_board()
    cur = {'L': (3, 0), 'R': (3, 2)}
    answer = ''

    for num in numbers:
        
        if num in LEFT_SIDE:
            answer += 'L'
            cur['L'] = board[num]
        
        elif num in RIGHT_SIDE:
            answer += 'R'
            cur['R'] = board[num]
        
        else:
            next_hand = get_next_hand(cur, board[num], hand)
            answer += next_hand
            cur[next_hand] = board[num]
    return answer

if __name__ == '__main__':
    result = solution(
        [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
        "right"
    )
    print(result)