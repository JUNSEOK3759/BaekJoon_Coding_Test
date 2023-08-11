def solution(n):
    answer = 0
    
    while n:
        x = n % 10
        answer += x
        n = n // 10
    

    return answer