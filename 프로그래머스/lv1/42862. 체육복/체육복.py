from collections import deque
def solution(n, lost, reserve):
    reserve1 = list(set(reserve) - set(lost))
    lost1 = list(set(lost) - set(reserve))
    
    for i in reserve1:
        a, b = i-1, i+1
        if a in lost1:
            lost1.remove(a)
        elif b in lost1:
            lost1.remove(b)
            
    return n-len(lost1)