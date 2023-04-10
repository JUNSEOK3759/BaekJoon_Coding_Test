from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    a = deque(A)
    B.sort()
    while True:
        for i in range(len(B)):
            if B[i] > a[0]:
                B[i] = 0
                answer += 1
                a.popleft()
        else:
            break    
    return answer