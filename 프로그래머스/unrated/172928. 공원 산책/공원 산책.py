from collections import deque
def solution(park, routes):
    answer = []
    len_x = len(park)
    len_y = len(park[0])
    
    def bfs(i, j, answer):
        dq = deque()
        dq.append([i, j])
        answer = [i, j]
        cnt = 0
        while dq and cnt < len(routes):
            x, y = dq.popleft()
            z, w = routes[cnt].split(' ')
            cnt += 1
            w = int(w)
            if z == 'E' and -1 < y+w < len_y:
                for i in range(y, y+w+1):
                    if park[x][i] == 'X':
                        dq.append([x, y])
                        break
                else:
                    dq.append([x, y+w])
                    answer = [x, y+w]
            elif z == 'W' and -1 < y-w < len_y:
                for i in range(y-w, y+1):
                    if park[x][i] == 'X':
                        dq.append([x, y])
                        break
                else:
                    dq.append([x, y-w])
                    answer = [x, y-w]
                    
            elif z == 'S' and -1 < x+w < len_x:
                for i in range(x, x+w+1):
                    if park[i][y] == 'X':
                        dq.append([x, y])
                        break
                else:
                    dq.append([x+w, y])
                    answer = [x+w, y]
                    
            elif z == 'N' and -1 < x-w < len_x:
                for i in range(x-w,x+1):
                    if park[i][y] == 'X':
                        dq.append([x, y])
                        break
                else:
                    dq.append([x-w, y])
                    answer = [x-w, y]

            else:
                dq.append([x, y])
                
        return answer
    
    
    for i in range(len_x):
        for j in range(len_y):
            if park[i][j] == 'S':
                res = bfs(i, j, answer)
                return res