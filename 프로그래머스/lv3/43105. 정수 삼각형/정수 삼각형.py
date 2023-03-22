from collections import deque
def solution(triangle):
    answer = 0
    length = len(triangle)
    ch = [[0 for _ in range(i+1)] for i in range(length+1)]
    dx = [1, 1]
    dy = [0, 1]
    ch[0][0] = triangle[0][0]
    res = -2147483647
    def bfs():
        dq = deque()
        dq.append([0,0])
        
        while dq:
            x, y = dq.popleft()
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < length and ny < length:
                    k = triangle[nx][ny] + ch[x][y]
                    if k > ch[nx][ny]:
                        ch[nx][ny] = k
                        dq.append([nx, ny])
    bfs()
    
    return max(map(max, ch))