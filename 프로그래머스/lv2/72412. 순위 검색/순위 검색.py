import itertools
import re
from bisect import bisect_left
def solution(info, query):
    answer = []
    infoDict = {}
    a = [1, 2, 3]
    for i in info:
        x = i.split(' ')
        a = x[:-1]
        b = int(x[-1])
        
        for j in range(5):
            for k in list(itertools.combinations(a, j)):
                res = ''.join(k)
                if res in infoDict:
                    infoDict[res].append(b)
                else:
                    infoDict[res] = [b]
    for i in infoDict:
        infoDict[i].sort()
        
    for i in query:
        x = re.sub(' and ', '', i)
        x = re.sub('-', '', x)
        x = x.split(' ')
        a = x[0]
        b = int(x[-1])

        
        if a in infoDict:
            score = infoDict[a]
            
            if score:
                res = bisect_left(score,b)
                answer.append(len(score) - res)
        else:
            answer.append(0)    
    return answer