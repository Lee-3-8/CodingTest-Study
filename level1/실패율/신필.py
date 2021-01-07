def solution(N, stages):
  stage_num = {}
  sum = len(stages)

  for i in range(1,N+1):
    stage_num[i] = 0

  for i in stages:
    if(i == N+1):
      continue
    stage_num[i] += 1

  for i in stage_num:
    if(sum == 0):
      continue
    print(i, stage_num[i],sum)
    temp = stage_num[i]
    stage_num[i] = stage_num[i]/sum
    sum -= temp

  answer = sorted(stage_num.items(), key=lambda x:x[1], reverse=True)
  answer = list(map(lambda x: x[0] , answer))
  print(answer)
  return answer

solution(5, [1,2,2,1,3])