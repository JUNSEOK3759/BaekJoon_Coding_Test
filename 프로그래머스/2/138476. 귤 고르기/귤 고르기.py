from collections import Counter
def solution(k, tangerine):
    answer = 0
    x = Counter(tangerine)
    a = sorted(x.values(), reverse = True)
    q = 0
    while k > 0:
        k -= a[q]
        q += 1
        answer += 1
    return answer