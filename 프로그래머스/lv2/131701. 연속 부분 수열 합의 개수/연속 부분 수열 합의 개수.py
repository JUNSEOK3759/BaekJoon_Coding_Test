def solution(elements):
    len_e = len(elements)
    res = set()

    for i in range(len_e):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+len_e):
            ssum += elements[j%len_e]
            res.add(ssum)
    return len(res)

def solution2(elements):
    answer = 0
    q = elements * 2
    a = 1
    x = set()
    while a <= len(elements):
        for i in range(len(q)):
            x.add(sum(q[i : i+a]))
        a += 1
    return len(x)
    