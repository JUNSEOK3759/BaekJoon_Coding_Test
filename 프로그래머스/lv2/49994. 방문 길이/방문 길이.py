def solution(dirs):
    move = {'U' : [0, 1], 'D' : [0, -1], 'L' : [-1, 0], 'R' : [1, 0]}
    a = set()
    point = (0, 0)
    for i in dirs:
        x = point
        if  -5 <= point[0] + move[i][0] <= 5 and -5 <= point[1] + move[i][1] <= 5:
            point = list(point)
            point[0] += move[i][0]
            point[1] += move[i][1]
            point = tuple(point)
            k = ((x, point), (point, x))
            k = tuple(sorted(k))
            a.add(k)
    return len(a)