def solution(n):
    answer = 0
    a = [0] * n
    for i in range(2, n + 1):
        for j in range(i+i, n+1, i):
            a[j-1] = 1
        
    answer = a.count(0) -1
        
    return answer