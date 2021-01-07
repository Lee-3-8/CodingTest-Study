def add_zero(n,str):
  if(len(str)<n):
    add = ' '*(n-len(str))
    return add + str
  else:
    return str
def solution(n, arr1, arr2):
  print(format(31 | 14,'b'))
  #리스트 내포 , bin()을 쓰면 앞에  0b가붙어서 저거씀
  result = [add_zero(n,format((x | y),'b').replace('1','#').replace('0',' ')) for x,y in zip(arr1,arr2)] 
  print(result)
  return result

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))