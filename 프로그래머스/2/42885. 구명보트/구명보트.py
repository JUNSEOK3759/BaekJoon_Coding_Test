from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    a = deque(people)
    
    while len(a) >= 2:
        if a[0] + a[-1] <= limit:
                a.pop()
                a.popleft()
        else:
            a.pop()
        answer += 1
    if a:
        answer += 1
    return answer