EMPTY, CHECK = '@', '#'

def remove_block(m, n, board):
    removed = False
    check_list = []

    for i in range(m - 1):
        for j in range(n - 1):
            if (
                board[i][j] != EMPTY and
                board[i][j] == board[i + 1][j] and
                board[i][j] == board[i + 1][j + 1] and
                board[i][j] == board[i][j + 1]
            ):
                removed = True
                check_list.append((i, j))

    for i, j in check_list:
        board[i][j], board[i][j+1] = EMPTY, EMPTY
        board[i+1][j], board[i+1][j+1] =  EMPTY, EMPTY 

    return removed

def fill_block(m, n, board):
    for j in range(n):
        for i in reversed(range(m)):
            if board[i][j] != EMPTY:
                tg_i = i
                while tg_i + 1 < m and board[tg_i + 1][j] == EMPTY:
                    tg_i += 1
                board[i][j], board[tg_i][j] = board[tg_i][j], board[i][j]

def solution(m, n, board):
    board = [list(i) for i in board]
    while remove_block(m, n, board):
        fill_block(m, n, board)
    return sum([line.count(EMPTY) for line in board])



if __name__ == '__main__':
    # print(
    #     solution(4, 5,
    #         ["CCBDE",
    #          "AAADE",
    #          "AAABF",
    #          "CCBBF"]
    #     )
    # )
    print(
        solution(6, 6,
            ["TTTANT",
             "RRFACC",
             "RRRFCC",
             "TRRRAA",
             "TTMMMF",
             "TMMTTJ"]
        )
    )