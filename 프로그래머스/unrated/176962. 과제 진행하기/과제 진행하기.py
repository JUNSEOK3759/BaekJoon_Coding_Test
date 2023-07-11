from collections import deque
def solution(plans):
    answer = []
    
    def makeNewList(plans):
        for i in range(len(plans)):
            x, y, z = plans[i]
            a, b = y.split(':')
            y = int(a) * 60 + int(b)
            z = int(z)
            plans[i] = [x, y, y+z]
        
    
    makeNewList(plans)
    plans.sort(key = lambda x : x[1])
    a = deque(plans)
    stack = []
    
    while a:
        if len(a) >= 2 and a[0][2] > a[1][1]:
            x, y, z = a.popleft()
            stack.append([x, z - a[0][1]])
        else:
            x, y, z = a.popleft()
            answer.append(x)
            
            if stack:
                i, j = stack.pop()
                a.appendleft([i, z, z+j])
    return answer