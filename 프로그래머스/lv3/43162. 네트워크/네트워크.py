from collections import deque
def solution(n, computers):
    answer = 0
    
    ch = [0 for _ in range(n)]
    
    def bfs(x):
        dq = deque()
        dq.append(x)
        ch[x] = 1
        
        while dq:
            x = dq.popleft()
            
            for i in range(n):
                if i != x and computers[x][i] == 1:
                    if ch[i] == 0:
                        ch[i] = 1
                        dq.append(i)
        
    for i in range(n):
        if ch[i] == 0:
            bfs(i)
            answer += 1
    return answer