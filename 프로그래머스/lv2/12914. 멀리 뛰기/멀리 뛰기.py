def solution(n):
    a, b = 0, 1
    for _ in range(n+1):
        a, b = b, a + b
    return a % 1234567