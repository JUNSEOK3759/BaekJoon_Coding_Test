def dictionary(records):
    dic = {}
    for i in records:
        x, y, z = i.split()
        if y in dic:
            dic[y].append(x)
        else:
            dic[y] = [x]
    dic = sorted(dic.items())
    return dict(dic)

import math
def solution(fees, records):
    answer = []
    dic = dictionary(records)
    print(dic)
    for key, value in dic.items():
        for i in range(len(value)):
            t, m = value[i].split(':')
            value[i] = (int(t)*60) + int(m)
        tot = 0
        for i in range(0, len(value), 2):
            try:
                tot += value[i+1] -value[i]
            except IndexError:
                tot += (60*24) - 1 - value[i]
        if tot > fees[0]:       
            answer.append(fees[1] + math.ceil((tot - fees[0]) / fees[2]) *fees[3])
        else:
            answer.append(fees[1])
    return answer