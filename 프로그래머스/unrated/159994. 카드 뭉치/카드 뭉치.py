from collections import deque
def solution(cards1, cards2, goal):
    c1 = deque(cards1)
    c2 = deque(cards2)
    for i in goal:
        if c1 and i == c1[0]:
            c1.popleft()
        elif c2 and i == c2[0]:
            c2.popleft()
        else:
            return 'No'
    return 'Yes'