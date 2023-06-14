from collections import deque
def solution(maps):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    len_x = len(maps)
    len_y = len(maps[0])
    ch = [[0 for _ in range(len_y)] for _ in range(len_x)]
    def bfs(x, y):
        dq = deque()
        dq.append([x, y])
        cnt = int(maps[x][y])
        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < len_x and -1 < ny < len_y and maps[nx][ny] != 'X':
                    if ch[nx][ny] == 0:
                        ch[nx][ny] = 1
                        cnt += int(maps[nx][ny])
                        dq.append([nx,ny])
        return cnt
    
    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] != 'X' and ch[i][j] == 0:
                ch[i][j] = 1
                answer.append(bfs(i, j))
            
    return sorted(answer) if answer else [-1]