def solution(n):
    a = [0 for _ in range(n+1)]
    a[1] = 1
    
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[-1] % 1234567