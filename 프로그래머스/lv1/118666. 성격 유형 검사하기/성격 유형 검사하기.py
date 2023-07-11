'''
1 : r, t
2 : c, f
3 : j, m
4 : a, n
'''
def solution(survey, choices):
    answer = ''
    a = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        x, y = survey[i][0], survey[i][1]
        z = choices[i]
        if z>= 5:
            a[y] += z-4
        elif z < 4:
            a[x] += 4 - z
    
    res = [i for i in a.values()]
    alp = [i for i in a.keys()]
    
    for i in range(0, len(res), 2):
        if res[i] >= res[i+1]:
            answer += alp[i]
        else:
            answer += alp[i+1]
    return answer