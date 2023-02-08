from collections import deque
def solution(maps):
    dq = deque()
    dq.append([0, 0, 1])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    len_x , len_y = len(maps), len(maps[0])
    while dq:
        x, y, d = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx > -1 and ny > -1 and nx < len_x and ny < len_y and maps[nx][ny] == 1:
                maps[nx][ny] = d + 1
                dq.append([nx, ny, maps[nx][ny]])
    for i in maps:
        print(i)
    if maps[-1][-1] not in [0, 1]:
        return maps[-1][-1]
    else:
        return -1