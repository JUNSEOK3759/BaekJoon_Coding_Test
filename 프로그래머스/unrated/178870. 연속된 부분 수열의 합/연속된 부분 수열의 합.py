def solution(a, k):
    answer = []
    
    if k in a:
        x = a.index(k)
        return [x, x]
    tot = a[0]
    lt = 0
    rt = 0
    
    while True:
        if lt == len(a)-1:
            break
        if tot == k:
            answer.append([lt, rt])
            tot -= a[lt]
            lt += 1
            
        elif tot < k:
            if rt < len(a)-1:
                rt += 1
                tot += a[rt]
            else:
                break
        else:
            tot -= a[lt]
            lt += 1
    answer.sort(key = lambda x : ((x[1]-x[0], x[0])))
    return answer[0]