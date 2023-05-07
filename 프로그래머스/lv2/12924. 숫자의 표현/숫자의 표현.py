def solution(n):
    answer = 0
    a = []
    for i in range(n, 0, -1):
        a.append(i)
        if sum(a) < n:
            continue
        elif sum(a) == n:
            a.pop(0)
            answer += 1
        else:
            a.pop(0)
    return answer