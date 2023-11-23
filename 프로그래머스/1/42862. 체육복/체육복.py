def solution(n, lost1, reserve1):
    answer = 0
    reserve = list(set(reserve1) - set(lost1))
    lost = list(set(lost1)- set(reserve1))
    reserve.sort()
    lost.sort()
    
    for i in reserve:
        front = i-1
        back = i+1
        if front in lost:
            lost.remove(front)
        elif back in lost:
            lost.remove(back)
        
    return n - len(lost)