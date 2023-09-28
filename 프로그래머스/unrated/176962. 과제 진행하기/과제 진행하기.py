from collections import deque
def makeTimeInt(plans):
    for i in range(len(plans)):
        x, y, z = plans[i]
        y1, y2 = y.split(":")
        start = (int(y1) * 60) + int(y2)
        end = start + int(z)
        plans[i] = [x, start, end]
    return

def solution(plans):
    answer = []
    makeTimeInt(plans)
    plans.sort(key = lambda x : (x[1], x[2]))
    p = deque(plans)
    stack = []
    
    while p:
        if len(p) >= 2 and p[0][2] > p[1][1]:
            x, y, z = p.popleft()
            stack.append([x, z - p[0][1]])
        else:
            x, y, z = p.popleft()
            answer.append(x)
            if stack:
                i, j = stack.pop()
                p.appendleft([i, z, z + j])
    return answer