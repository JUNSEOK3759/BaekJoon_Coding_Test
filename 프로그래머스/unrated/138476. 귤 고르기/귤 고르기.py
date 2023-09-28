from collections import Counter
def solution(k, tangerine):
    answer = 0
    a = Counter(tangerine)
    a = [[x, y] for x, y in a.items()]
    a.sort(key = lambda x : (-x[1], x[0]))
    
    for x, y in a:
        if k <= 0:
            break
        k -= y
        answer += 1
    return answer