from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, len_x, len_y, maps, ch):
    dq = deque()
    d = int(maps[x][y])
    dq.append([x, y])
    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < len_x and -1 < ny < len_y and ch[nx][ny] == 0 and maps[nx][ny].isdigit():
                ch[nx][ny] = 1
                d += int(maps[nx][ny])
                dq.append([nx, ny, ])
    return d
    

def solution(maps):
    answer = []
    len_x = len(maps)
    len_y = len(maps[0])
    ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
    
    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j].isdigit() and ch[i][j] == 0:
                ch[i][j] = 1
                answer.append(bfs(i, j, len_x, len_y, maps, ch))
    return sorted(answer) if answer else [-1]