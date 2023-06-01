from collections import deque
def solution(plans):
    answer = []
    
    def makeNewList(plans):
        a = []
        for i in plans:
            x, y, z = i[0], i[1], i[2]
            y1, y2 = y.split(':')
            y1, y2,z = int(y1), int(y2), int(z)
            summ = y1 * 60 + y2
            a.append([x, summ, summ + z])
        return a
    
    a = makeNewList(plans)
    a.sort(key = lambda x : (x[1]))
    a = deque(a)
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
                a.appendleft([i, z, z + j])
                
    return answer