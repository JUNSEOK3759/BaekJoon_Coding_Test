def makeBinary(n):
    s = ''
    while n:
        s += str(n%2)
        n = n//2
    return s[::-1]

def solution(n):
    answer = 0
    x = makeBinary(n)
    cnt = 0
    for i in range(n+1, 1000000):
        y = makeBinary(i)
        if x.count('1') == y.count('1'):
            return i