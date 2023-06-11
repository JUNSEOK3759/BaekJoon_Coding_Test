def solution(dirs):
    answer = set()
    x = {'U' : [0, 1], 'D' : [0, -1], 'L' : [-1, 0], 'R' : [1, 0]}
    s = (0, 0)
    for i in dirs:
        nx = s[0] + x[i][0]
        ny = s[1] + x[i][1]
        if -6 < nx < 6 and -6 < ny < 6:
            answer.add(tuple(sorted(((s[0],s[1]),(nx,ny)))))
            s = (nx, ny)
    return len(answer)