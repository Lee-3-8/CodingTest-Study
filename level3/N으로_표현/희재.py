def solution(n, number, answer=-1):
	paste = lambda x, num: int(str(x) * num)
	operate = lambda a, b: [a+b, a-b, a*b, a//b if b != 0 else 0]
	dp = [None]

	for i in range(1, 8 + 1):
		cur_set = set([paste(n, i)])
		for a_idx, b_idx in zip(range(1, i), range(i - 1, 0, -1)):
			for a_num in dp[a_idx]:
				for b_num in dp[b_idx]:
					cur_set.update(operate(a_num, b_num))
		if number in cur_set:
			return i
		dp.append(cur_set)

	return answer

if __name__ == '__main__':
	print(solution(5, 12))