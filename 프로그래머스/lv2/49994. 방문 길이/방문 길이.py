def solution(dirs):
    answer = set()
    x = {'U' : [0, 1], 'D' : [0, -1], 'L' : [-1, 0], 'R' : [1, 0]}
    a = (0, 0)
    for i in dirs:
        nx = a[0] + x[i][0]
        ny = a[1] + x[i][1]
        if nx > -6 and nx < 6 and ny > -6 and ny < 6:
            answer.add(tuple(sorted(((a[0],a[1]),(nx,ny)))))
            a = (nx, ny)
    return len(answer)