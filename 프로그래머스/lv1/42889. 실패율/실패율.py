def solution(N, stages):
    
    answer = []
    a = {}
    x = len(stages)
    for i in range(1, N+1):
        if x != 0:
            y = stages.count(i)
            a[i] = stages.count(i) / x
            x -= y
        else:
            a[i] = 0
            
            
    return sorted(a, key = lambda k : a[k], reverse = True)