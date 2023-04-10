from collections import deque
def solution(queue1, queue2):
    answer = 0
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    sum1 = sum(deq1)
    sum2 = sum(deq2)
    while sum1 != sum2:
        answer += 1
        if sum1 > sum2:
            x = deq1.popleft()
            deq2.append(x)
            sum1 -= x
            sum2 += x
        else:
            y = deq2.popleft()
            deq1.append(y)
            sum1 += y
            sum2 -= y
        if answer == len(deq1) * 2:
            return -1
    return answer