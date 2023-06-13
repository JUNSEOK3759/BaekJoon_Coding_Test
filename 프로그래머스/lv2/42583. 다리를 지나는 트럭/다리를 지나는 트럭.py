from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights = deque(truck_weights)
    bw = sum(bridge)
    while bridge:
        answer += 1
        y = bridge.popleft()
        bw -= y
        if truck_weights:
            if bw + truck_weights[0] <= weight:
                x = truck_weights.popleft()
                bridge.append(x)
                bw += x
            else:
                bridge.append(0)
    return answer