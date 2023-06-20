from collections import deque
def solution(park, routes):
    len_x, len_y = len(park), len(park[0])
    move = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    
    def bfs(i, j):
        dq = deque()
        dq.append([i, j])
        res = [i, j]
        cnt = 0
        while dq and cnt < len(routes):
            x, y = dq.popleft()
            a, b = routes[cnt].split(' ')
            cnt += 1
            nx = x + (move[a][0] * int(b))
            ny = y + (move[a][1] * int(b))
            if -1 < nx < len_x and -1 < ny < len_y:
                if a == 'E':
                    for j in range(y, ny+1):
                        if park[nx][j] == 'X':
                            dq.append([x, y])
                            break
                    else:
                        dq.append([nx, ny])
                        res = [nx, ny]
                elif a == 'W':
                    for j in range(ny, y+1):
                        if park[nx][j] == 'X':
                            dq.append([x, y])
                            break
                    else:
                        dq.append([nx, ny])
                        res = [nx, ny]
                elif a == 'S':
                    for j in range(x, nx+1):
                        if park[j][ny] == 'X':
                            dq.append([x, y])
                            break
                    else:
                        dq.append([nx, ny])
                        res = [nx, ny]
                elif a == 'N':
                    for j in range(nx, x+1):
                        if park[j][ny] == 'X':
                            dq.append([x, y])
                            break
                    else:
                        dq.append([nx, ny])
                        res = [nx, ny]
            else:
                dq.append([x, y]) 
        return res
    
    for i in range(len_x):
        for j in range(len_y):
            if park[i][j] == 'S':
                return bfs(i,j)