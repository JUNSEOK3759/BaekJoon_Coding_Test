from collections import deque
move = {'E' : [0, 1], 'W' : [0, -1], 'S' : [1, 0], 'N' : [-1, 0]}

def bfs(i, j, routes, len_x, len_y, park):
    
    dq = deque()
    dq.append([i, j])
    answer = [i, j]
    cnt = 0
    
    while dq and cnt < len(routes):
        x, y = dq.popleft()
        point, dis = routes[cnt].split(' ')
        cnt += 1
        dis = int(dis)
        if point == 'E' and -1 < y + dis < len_y:
            for i in range(y, y + dis+1):
                if park[x][i] == 'X':
                    dq.append([x, y])
                    break
            else:
                answer = [x, y + dis]
                dq.append([x, y + dis])
        
        elif point == 'W' and -1 < y - dis < len_y:
            for i in range(y - dis, y + 1):
                if park[x][i] == 'X':
                    dq.append([x, y])
                    break
            else:
                answer = [x, y - dis]
                dq.append([x, y - dis])
        
        elif point == 'S' and -1 < x + dis < len_x:
            for i in range(x, x + dis+1):
                if park[i][y] == 'X':
                    dq.append([x, y])
                    break
            else:
                answer = [x + dis, y]
                dq.append([x + dis, y])
                
        elif point == 'N' and -1 < x - dis < len_x:
            for i in range(x - dis, x + 1):
                if park[i][y] == 'X':
                    dq.append([x, y])
                    break
            else:
                answer = [x - dis, y]
                dq.append([x - dis, y])
        else:
            dq.append([x, y])
            
    return answer
    
    
def solution(park, routes):
    answer = []
    len_x = len(park)
    len_y = len(park[0])
    for i in range(len_x):
        for j in range(len_y):
            if park[i][j] == 'S':
                res = bfs(i, j, routes, len_x, len_y, park)
                return res