from collections import deque
def solution(n, m, section):
    answer = 0
    
    section = deque(section)
    
    while section:
        x = section.popleft()
        
        while section and x + m > section[0]:
            section.popleft()
        answer += 1
    return answer