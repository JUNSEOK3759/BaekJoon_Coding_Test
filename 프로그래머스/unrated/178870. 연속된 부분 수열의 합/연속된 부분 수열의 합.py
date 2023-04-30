from collections import deque
def solution(a, k):
    answer = []
    
    if k in a:
        x = a.index(k)
        return [x, x]
    sum = a[0]
    lt = 0
    rt = 0
    while True:
        if lt == len(a)-1:
            break
        if sum < k:
            if rt < len(a)-1:
                rt += 1
                sum += a[rt]
            else:
                break
        elif sum > k:
            sum -= a[lt]
            lt += 1
            
        else:
            if not answer or rt - lt < answer[1] - answer[0]:
                answer = [lt, rt]
            sum -= a[lt]
            lt += 1
                
    return answer