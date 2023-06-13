import math
def solution(fees, records):
    
    def timer(x):
        a, b = x.split(':')
        y = int(a) * 60 + int(b)
        return y
    
    answer = []
    a = {}
    for i in records:
        x, y, z = i.split()
        x = timer(x)
        if y not in a:
            a[y] = [x]
        else:
            a[y].append(x)
    res = []
    
    for x, y in a.items():
        q = [x]
        w = 0
        if len(y) % 2 != 0:
            a[x].append(60*24 - 1)
        for i in range(0, len(y), 2):
            w += abs(y[i+1] - y[i])
        if w > fees[0]:
            w = math.ceil((w-fees[0]) / fees[2]) * fees[3]
        else:
            w = 0
        q.append(fees[1] + w)
        res.append(q)
    res.sort()
    
    for i in res:
        answer.append(i[1])
    
    return answer