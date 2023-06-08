def solution(dartResult):
    answer = 0
    mul = {'S' : 1, 'D' : 2, 'T' : 3}
    res = []
    x = ''
    for i in dartResult:
        if i.isdigit():
            x += str(i)
        elif i in ['S','D','T']:
            if x.isdigit():
                x = int(x) ** mul[i]
                res.append(x)
                x = ''
        else:
            if i == '*':
                if len(res) >= 2:
                    res[-1], res[-2] = 2*res[-1], 2*res[-2]
                else:
                    res[-1] = 2*res[-1]
            elif i == '#':
                res[-1] = -res[-1]
    return sum(res)