from math import ceil

def solution(ps, ss):
    answer = []
    times = [ceil((100 - p) / s) for p, s in zip(ps, ss)]
    cur_max, cur_cnt = times[0], 1
    
    for time in times[1:]:
    	if time <= cur_max:
    		cur_cnt += 1
    	else:
    		answer.append(cur_cnt)
    		cur_max, cur_cnt = time, 1

    return answer + [cur_cnt]

if __name__ == '__main__':
	print(solution([93, 30, 55], [1, 30, 5]))