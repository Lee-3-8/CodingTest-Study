from itertools import permutations

def get_board(max_num):
    board = [True for i in range(max_num + 1)]
    board[0], board[1] = False, False

    for i in range(2, int(max_num ** 0.5) + 1):
        if board[i]:
            j = 2
            while i * j <= max_num:
                board[i * j] = False
                j += 1

    return board

def solution(numbers):
    max_num = int("".join(sorted(numbers, reverse=True)))
    board = get_board(max_num)

    perms = []
    for i in range(1, len(numbers) + 1):
        perms_i = map(lambda x: int("".join(x)), permutations(numbers, i))
        perms.extend(perms_i)

    return sum(board[perm] for perm in set(perms))

if __name__ == '__main__':
    print(solution("011"))