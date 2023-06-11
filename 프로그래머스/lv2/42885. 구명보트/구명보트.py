from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    x = deque(people)
    
    
    while len(x) > 1:
        answer += 1
        if x[0] + x[-1] <= limit:
            x.popleft()
            x.pop()
        else:
            x.pop()
    if x:
        answer += 1
    return answer