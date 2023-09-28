def solution(n):
    answer = 1
    a = [i for i in range(1, n+1)]
    lt = 0
    rt = 1
    while lt <= rt:
        if lt == len(a)-1:
            break
        x = sum(a[lt:rt])
        if x == n:
            answer += 1
            lt += 1
        elif x > n:
            lt += 1
        else:
            rt += 1
        
    return answer