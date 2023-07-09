import itertools
from collections import Counter
def solution(a):
    answer = 0
    a.sort()
    diction = Counter(a)
    
    for i in diction.values():
        if i == 2:
            answer += 1
        else:
            answer += i *(i-1) // 2
    
    l, m, n = 4, 3, 2 
    a = sorted(list(set(a)))
    for com in itertools.combinations(a, 2):
        q, w = com
        if q * l == w * m or q * l == w * n or q * m == w * n:
            answer += diction[q] * diction[w]
    return answer