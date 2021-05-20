
def solution(n, times):
    def search(left, right):
    	mid = (left + right) // 2
    	if left >= right:
    		return left
    	elif sum([mid // t for t in times]) >= n:
    		return search(left, mid)
    	else:
    		return search(mid + 1, right)

    return search(1, max(times) * n)

if __name__ == '__main__':
	print(solution(6, [7, 10]))
	print(solution(3, [1, 1, 1]))
	print(solution(3, [1, 2, 3]))