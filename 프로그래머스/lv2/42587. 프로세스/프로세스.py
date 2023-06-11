from collections import deque
def solution(priorities, location):
    answer = []
    a = [chr(i) for i in range(97, 97+len(priorities))]
    a = deque(a)
    p = deque(priorities)
    x = a[location]
    while p and a:
        
        if answer and answer[-1][0] == x:
            break
        
        if max(p) != p[0]:
            a.append(a.popleft())
            p.append(p.popleft())
        else:
            answer.append([a.popleft(), p.popleft()])
            
    return len(answer)