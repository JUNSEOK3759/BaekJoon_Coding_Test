from collections import deque
def solution(queue1, queue2):
    answer = 0
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    sumDeq1 = sum(deq1)
    sumDeq2 = sum(deq2)
    while sumDeq1 != sumDeq2:
        answer += 1
        if sumDeq1 > sumDeq2:
            x = deq1.popleft()
            deq2.append(x)
            sumDeq1 -= x
            sumDeq2 += x
        else:
            x = deq2.popleft()
            deq1.append(x)
            sumDeq2 -= x
            sumDeq1 += x
        if answer == len(deq1) * 2:
            answer = -1
            break
    return answer