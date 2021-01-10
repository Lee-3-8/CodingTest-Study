n=6
def solution(n):
    end=int((n*(n+1)/2))
    answer = [0 for i in range(end)]
    counter=2
    raise_cnt=1
    m=1
    bottom_cnt=0
    top_cnt=n
    recursive_top=0
    total_number=n
    answer[0]=1
    while end!=counter-1:
        raise_cnt=m
        for i in range(total_number):
            if(end==counter-1 or bottom_cnt==n*(n-1)/2):
                break
            bottom_cnt+=raise_cnt
            raise_cnt+=1
            answer[bottom_cnt]=counter
            counter+=1
        total_number-=1
        for i in range(total_number):
            if(end==counter-1):
                break
            bottom_cnt+=1
            answer[bottom_cnt]=counter
            counter+=1
        total_number-=1
        recursive_top=top_cnt
        for i in range(total_number):
            if(end==counter-1):
                break
            bottom_cnt-=recursive_top
            answer[bottom_cnt]=counter
            counter+=1
            recursive_top-=1   
        top_cnt-=1
        total_number-=1
        if(bottom_cnt==2):
            m+=1
        else:
            m+=2
         
    return answer

print(solution(n))