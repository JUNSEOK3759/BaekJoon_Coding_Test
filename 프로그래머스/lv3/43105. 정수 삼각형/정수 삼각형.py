def solution(t):
    for i in range(1, len(t)):
        t[i][0] += t[i-1][0]
        t[i][i] += t[i-1][i-1]
        for j in range(1, i):
            t[i][j] += max(t[i-1][j], t[i-1][j-1])
    return max(t[-1])