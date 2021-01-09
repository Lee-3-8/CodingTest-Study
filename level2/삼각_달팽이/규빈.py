def solution(n):
    answer = []
    arr = [[0 for col in range(row + 1)] for row in range(n)]
    row = 0
    col = 0
    loof = n
    count = 1
    while(loof > 0):
        for j in range(loof):
             arr[row][col] = count
             row += 1
             count += 1
        row -= 1
        col += 1
        loof -= 1

        for j in range(loof):
            arr[row][col] = count
            col += 1
            count += 1
        col -= 2
        row -= 1
        loof -= 1

        for j in range(loof):
            arr[row][col] = count
            row -= 1
            col -= 1
            count += 1
        row += 2
        col += 1
        loof -= 1
        
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])

    return answer


print(solution(6))
