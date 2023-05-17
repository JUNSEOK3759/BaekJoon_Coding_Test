def solution(cacheSize, cities):
    answer = 0
    a = []
    for i in cities:
        i = i.lower()
        if i not in a:
            if len(a) < cacheSize:
                a.append(i)
            else:
                a.append(i)
                a.pop(0)
                
            answer += 5
        else:
            answer += 1
            a.pop(a.index(i))
            a.append(i)
    return answer