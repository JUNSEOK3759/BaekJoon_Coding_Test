from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    len_x, len_y = len(maps), len(maps[0])
    
    
    def lbfs(x, y):
        dq = deque()
        dq.append([x, y])
        ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if -1 < nx < len_x and -1 < ny < len_y and ch[nx][ny] == 0:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'E':
                        ch[nx][ny] = ch[x][y] + 1
                        dq.append([nx, ny])
                    elif maps[nx][ny] == 'L':
                        return ch[x][y] + 1
                
    def ebfs(x, y):
        dq = deque()
        dq.append([x, y])
        ch2 = [[0 for _ in range(len_y)] for _ in range(len_x)]
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < len_x and -1 < ny < len_y and ch2[nx][ny] == 0:
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'S':
                        ch2[nx][ny] = ch2[x][y] + 1
                        dq.append([nx, ny])
                    elif maps[nx][ny] == 'E':
                        return ch2[x][y] + 1
    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] == 'S':
                L = lbfs(i,j)
            if maps[i][j] == 'L':
                E = ebfs(i, j)
    return L + E if L and E else -1