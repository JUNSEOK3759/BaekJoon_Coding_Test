def solution(wallpaper):
    answer = [2147483647, 2147483647, -2147483647, -2147483647]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)
                answer[2] = max(answer[2], i)
                answer[3] = max(answer[3], j)
    answer[2] += 1
    answer[3] += 1
    return answer