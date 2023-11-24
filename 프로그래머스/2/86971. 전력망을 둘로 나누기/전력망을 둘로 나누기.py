from collections import deque
def bfs(k, n, a):
    dq = deque()
    dq.append(k)
    ch = [0 for _ in range(n+1)]
    ch[k] = 1
    cnt = 1
    
    while dq:
        x = dq.popleft()
        for i in a[x]:
            if ch[i] == 0:
                ch[i] = 1
                dq.append(i)
                cnt += 1
    return cnt

def solution(n, wires):
    answer = 2147483647
    a = [[] for _ in range(n+1)]
    
    for x, y in wires:
        a[x].append(y)
        a[y].append(x)
    
    for x, y in wires:
        a[x].remove(y)
        a[y].remove(x)
        answer = min(abs(bfs(x, n, a)- bfs(y, n, a)), answer)
        a[x].append(y)
        a[y].append(x)
    return answer