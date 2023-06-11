def solution(elements):
    answer = 0
    q = elements * 2
    a = 1
    x = set()
    while a <= len(elements):
        for i in range(len(q)):
            x.add(sum(q[i : i+a]))
        a += 1
    return len(x)
    