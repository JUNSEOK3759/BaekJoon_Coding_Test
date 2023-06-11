from collections import Counter
def solution(k, tangerine):
    answer = 0
    x = Counter(tangerine)
    a = []
    for x, y in x.items():
        a.append([x, y])
    a.sort(key = lambda x : (x[1]), reverse = True)
    cnt = 0
    while k > 0:
        k -= a[cnt][1]
        answer += 1
        cnt += 1
    return answer