def solution(name, yearning, photo):
    answer = []
    a = {}
    for i in range(len(name)):
        a[name[i]] = yearning[i]
    
    for i in photo:
        res = 0
        for j in i:
            if j in a:
                res += a[j]
        answer.append(res)
    
    return answer