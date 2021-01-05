def solution(d, budget):
    answer = 0
    for money in sorted(d):
    	if money <= budget:
    		budget -= money
    		answer += 1
    return answer


if __name__ == '__main__':
	result = solution(
		[1,2,3,5,4],
		9
	)
	print(result)