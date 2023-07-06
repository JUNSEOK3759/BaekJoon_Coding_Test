import itertools
def solution(a):
    answer = 0
    a.sort()
    cnt = 0
    diction = {}
    while cnt < len(a):
        x = a.count(a[cnt])
        diction[a[cnt]] = x
        if x > 1:
            if x == 2:
                answer += 1
            else:
                answer += x * (x-1) // 2
            cnt += x
        else:
            cnt += 1
    l, m, n = 4, 3, 2 
    a = sorted(list(set(a)))
    for com in itertools.combinations(a, 2):
        q, w = com
        if q == w:
            continue
        elif q * l == w * m or q * l == w * n or q * m == w * n:
            answer += diction[q] * diction[w]
    return answer