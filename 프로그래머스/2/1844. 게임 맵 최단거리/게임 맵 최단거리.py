from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, len_x, len_y, maps):
    dq = deque()
    dq.append([x, y])
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1< nx < len_x and -1 < ny < len_y and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                dq.append([nx, ny])
                    
                
def solution(maps):
    answer = 0
    len_x = len(maps)
    len_y = len(maps[0])
    
    bfs(0, 0, len_x, len_y, maps)
    
    return maps[-1][-1] if maps[-1][-1] != 1 else -1