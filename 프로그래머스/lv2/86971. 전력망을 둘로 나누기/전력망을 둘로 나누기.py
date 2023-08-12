from collections import deque
def solution(n, wires):
    answer = 2147483647
    
    a = [[] for _ in range(n+1)]
    
    for x, y in wires:
        a[x].append(y)
        a[y].append(x)
    
    def bfs(k):
        dq = deque()
        dq.append(k)
        cnt = 1
        ch = [0 for _ in range(n+1)]
        ch[k] = 1
        
        while dq:
            x = dq.popleft()
            
            for i in a[x]:
                if ch[i] == 0:
                    ch[i] = 1
                    dq.append(i)
                    cnt += 1
        return cnt
    for x, y in wires:
        a[x].remove(y)
        a[y].remove(x)
        
        answer = min(abs(bfs(x) - bfs(y)), answer)
        
        a[x].append(y)
        a[y].append(x)
        
    return answer