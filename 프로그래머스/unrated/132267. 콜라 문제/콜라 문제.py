def solution(a, b, n):
    answer = 0
    div = 0
    while n:
        x = ((n + div) // a) * b
        y = (n + div) % a
        if y == 0:
            n = x
            answer += x
            div = 0
        else:
            n = x
            answer += x
            div = y
        
    return answer