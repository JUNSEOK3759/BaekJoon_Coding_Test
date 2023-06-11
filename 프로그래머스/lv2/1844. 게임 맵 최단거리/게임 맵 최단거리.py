from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    len_x = len(maps)
    len_y = len(maps[0])
    
    def bfs(x, y):
        dq = deque()
        dq.append([x, y])
        
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if -1 < nx < len_x and -1 < ny < len_y and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    dq.append([nx, ny])
    
    bfs(0, 0)
    return maps[-1][-1] if maps[-1][-1] != 1 else -1