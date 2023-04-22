def solution(n):
    answer = ''
    x = ['4', '1', '2']
    
    while True:
        a = n // 3
        b = n % 3
        if a > 0 and b == 0:
            a -= 1
        answer = x[b] + answer
        n = a
        if a == 0:
            break
    return answer