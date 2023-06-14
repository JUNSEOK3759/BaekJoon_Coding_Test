from collections import deque
def solution(queue1, queue2):
    answer = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    s1, s2 = sum(dq1), sum(dq2)
    if s1 + s2 % 2 == 1:
        return -1
    cnt = 0
    length = len(dq1) + len(dq2)
    while s1 != s2:
        
        if answer == length+10:
            return -1
        if s1 > s2:
            x = dq1.popleft()
            s1 -= x
            dq2.append(x)
            s2 += x
        else:
            x = dq2.popleft()
            s2-=x
            dq1.append(x)
            s1 += x
        answer += 1
    
    return answer