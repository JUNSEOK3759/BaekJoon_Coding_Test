def solution(n):
    answer = 0
    a = [i for i in range(1, n+1)]
    lt = 0
    rt = 0
    
    while True:
        x = sum(a[lt : rt+1])
        if x == n:
            lt += 1
            rt = lt
            answer += 1
        elif x > n:
            lt += 1
        else:
            rt += 1
        if lt == len(a):
            break
    return answer