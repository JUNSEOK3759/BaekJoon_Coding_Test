def solution(cacheSize, cities):
    answer = 0
    x = []
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        i = i.lower()
        if i not in x:
            if len(x) == cacheSize:
                x.pop(0)
            x.append(i)
            answer += 5
        else:
            answer += 1
            x.remove(i)
            x.append(i)
            
    return answer