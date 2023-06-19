from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = deque(0 for _ in range(bridge_length))
    tw = deque(truck_weights)
    summ = sum(b)
    
    while b:
        answer += 1
        x = b.popleft()
        summ -= x
        if tw:
            if summ + tw[0] <= weight:
                y = tw.popleft()
                b.append(y)
                summ += y
            else:
                b.append(0)
            
    return answer