from collections import Counter
def solution(k, tangerine):
    answer = 0
    s = Counter(tangerine)
    a = []
    for x, y in s.items():
        a.append([x, y])
    cnt = 0
    a.sort(key = lambda x : x[1], reverse = True)
    while k > 0:
        k -= a[cnt][1]
        cnt += 1
        answer += 1
    
    return answer