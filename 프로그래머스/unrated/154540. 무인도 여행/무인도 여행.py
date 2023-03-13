def mapssplit(maps):
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        for j in range(len(maps[i])):
            if maps[i][j].isdigit():
                maps[i][j] = int(maps[i][j])
def bfs(x, y, len_x, len_y, maps):
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        dq = deque()
        dq.append([x, y])
        cnt = maps[x][y]
        maps[x][y] = 'X'
        while dq:
            x, y = dq.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx > -1 and ny > -1 and nx < len_x and ny < len_y:
                    if maps[nx][ny] != 'X':
                        cnt += maps[nx][ny]
                        maps[nx][ny] = 'X'
                        dq.append([nx, ny])
        return cnt

from collections import deque
def solution(maps):
    answer = []
    mapssplit(maps)
    
         
    len_x = len(maps)
    len_y = len(maps[0])
    for i in range(len_x):
        for j in range(len_y):
            if maps[i][j] != 'X':
                res = bfs(i, j, len_x, len_y, maps)
                answer.append(res)
    answer.sort()
    return answer if answer else [-1]