def solution(a, k):
    answer = []
    
    if k in a:
        x = a.index(k)
        return [x, x]
    
    lt = 0
    rt = 0
    sum = a[0]
    while True:
        if lt == len(a)-1:
            break
        if sum == k:
            answer.append([lt, rt])
            sum -= a[lt]
            lt += 1
        elif sum < k:
            if rt >= len(a)-1:
                break
            else:
                rt += 1
                sum += a[rt]
        else:
            sum -= a[lt]
            lt += 1
    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
    return answer[0]