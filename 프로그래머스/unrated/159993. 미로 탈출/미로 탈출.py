from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
                
                
def solution(maps):
    answer = 0
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    
    len_x = len(maps)
    len_y = len(maps[0])
    cnt = 0
    ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
    
    def bfs_L(x, y):
        dq = deque()
        dq.append([x, y])
        ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > -1 and ny > -1 and nx < len_x and ny < len_y and ch[nx][ny] == 0:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'E':
                        ch[nx][ny] = ch[x][y] + 1
                        dq.append([nx, ny])
                    elif maps[nx][ny] == 'L':
                        return ch[x][y] + 1
                    
    def bfs_E(x, y):
        dq = deque()
        dq.append([x, y])
        ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx > -1 and ny > -1 and nx < len_x and ny < len_y and ch[nx][ny] == 0:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'S':
                        ch[nx][ny] = ch[x][y] + 1
                        dq.append([nx, ny])
                    elif maps[nx][ny] == 'E':
                        return ch[x][y] + 1
    L = 0
    E = 0
    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] == 'S':
                L = bfs_L(i, j)
            elif maps[i][j] == 'L':
                E = bfs_E(i, j)
    
    # for i in range(len_x):
    #     for j in range(len_y):
    #         if maps[i][j] == 'L':
    #             E = bfs_E(i, j)
    #             break
                
    
    return L + E if L and E else -1