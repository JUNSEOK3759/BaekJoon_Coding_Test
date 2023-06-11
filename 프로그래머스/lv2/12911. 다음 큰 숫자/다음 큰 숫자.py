def solution(n):
    answer = 0
    def makeBinary(k):
        x = ''
        while k > 0:
            x += str(k % 2)
            k = k // 2
        return list(x[::-1])
    x = makeBinary(n)
    cnt = 1
    asd = x.count('1')
    while True:
        z = makeBinary(n + cnt)
        if z.count('1') == asd:
            return n+cnt
        else:
            cnt += 1
            