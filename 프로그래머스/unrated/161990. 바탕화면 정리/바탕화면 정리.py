def solution(wallpaper):
    answer = [2147483647, 2147483647, -2147483647, -2147483647]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < answer[0]:  
                    answer[0] = i
                if j < answer[1]:
                    answer[1] = j
                if i+1 > answer[2]:
                    answer[2] = i+1
                if j+1 > answer[3]:
                    answer[3] = j+1
    return answer