def solution(brown, yellow):
    for row in range(1,yellow+1):
        if yellow % row == 0:
            col = yellow // row
            if brown == (row + 2) * 2 + (col * 2):
                return [col+2, row+2]