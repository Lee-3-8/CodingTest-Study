def solution(arr):
    Len = len(arr)

    zeroNum = sum(arr[i].count(0) for i in range(Len))
    oneNum = sum(arr[i].count(1) for i in range(Len))
    answer = [zeroNum, oneNum]

    if needQuad(arr):
        return quad(arr, answer)
    
    return [zeroNum//(Len**2),oneNum//(Len**2)]

def quad(arr, answer):
    length = len(arr)
    if length < 2:
        return answer
    
    splitLen = length//2
    for i in range(4):
        splitArr =[]
        for j in range(splitLen):
            splitArr.append(arr[(i//2)*splitLen +j][(i%2)*splitLen : (i%2)*splitLen + splitLen])
        if needQuad(splitArr):
            quad(splitArr, answer)
        else:
            answer[splitArr[0][0]] -= (len(sum(splitArr, [])) - 1)

    return answer


def needQuad(arr):
    compare = arr[0][0]
    Len = len(arr)
    for i in range(Len):
        for j in range(Len):
            if compare != arr[i][j]:
                return True
                
    return False