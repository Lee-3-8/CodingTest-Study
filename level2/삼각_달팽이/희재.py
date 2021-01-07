def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    is_valid = lambda i, j: True if i < n and j < n else False 
    flag, i, j, cnt, total_len = "bottom", 0, 0, 1, n*(n+1)/2
    
    while cnt <= total_len:
    	answer[i][j] = cnt
    	cnt += 1

    	if flag == "bottom":
    		if is_valid(i+1, j) and not answer[i+1][j]:
    			i += 1
    		else:
    			j += 1
    			flag = "right"

    	elif flag == "right":
    		if is_valid(i, j+1) and not answer[i][j+1]:
    			j += 1
    		else:
    			i, j = i-1, j-1
    			flag = "diagonal"
    	else:
    		if is_valid(i-1, j-1) and not answer[i-1][j-1]:
    			i, j = i-1, j-1
    		else:
    			i += 1
    			flag = "bottom"	

    return sum(answer, [])

if __name__ == '__main__':
	result = solution(4)
	print(result)