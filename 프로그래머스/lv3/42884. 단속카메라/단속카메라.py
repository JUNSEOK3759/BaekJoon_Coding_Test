def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    camera = -300001
    for i in routes:
        if i[0] > camera:
            answer += 1
            camera = i[1]
    return answer