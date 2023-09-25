from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    b = deque([0 for _ in range(bridge_length)])
    tw = deque(truck_weights)
    summ = sum(b)
    
    while b:
        answer += 1
        x = b.popleft()
        summ -= x
        if tw:
            if tw[0] + summ <= weight:
                y = tw.popleft()
                summ += y
                b.append(y)
            else:
                b.append(0)
    return answer