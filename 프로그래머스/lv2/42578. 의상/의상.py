def solution(clothes):
    answer = 1
    a = {}
    for i in clothes:
        y, x = i
        if x not in a:
            a[x] = [y]
        else:
            a[x].append(y)
    
    for i in a.values():
        answer *= len(i) + 1
    return answer -1