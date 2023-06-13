def solution(n, t, m, p):
    conv1 = {10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    def makeConv(x):
        s = ''
        if x == 0:
            return '0'
        while x > 0:
            if x % n <= 9:
                s += str(x % n)
            else:
                s += conv1[x%n]
            x = x // n
        return s[::-1]
    answer = ''    
    for i in range(t*m):
        answer += makeConv(i)
        if len(answer) >= t*m:
            break
    res = ''
    for i in range(p-1, len(answer), m):
        res += answer[i]
        if len(res) == t:
            return res
    
    return answer