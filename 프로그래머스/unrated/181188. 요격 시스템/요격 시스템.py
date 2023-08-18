def solution(targets):
    answer = 0
    targets.sort(key = lambda x : (x[1], x[0]))
    s, e = 0, 0
    
    for i in targets:
        if i[0] >= e:
            answer += 1
            e = i[1]
    return answer