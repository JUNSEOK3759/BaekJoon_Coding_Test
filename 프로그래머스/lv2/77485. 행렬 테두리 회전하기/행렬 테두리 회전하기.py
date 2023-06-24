def solution(rows, columns, queries):
    answer = []
    a = [[(columns*j)+i+1 for i in range(columns)] for j in range(rows)]
    for i in queries:
        x1, y1, x2, y2 = i
        x1, y1, x2, y2 = x1-1 , y1-1 , x2-1 , y2-1 
        rightTop = a[x1][y2]
        leftBottom = a[x2][y1]
        mini = 2147483647
        for j in range(y2, y1, -1):
            a[x1][j] = a[x1][j-1]
            mini = min(a[x1][j], mini)
        for j in range(y1, y2):
            a[x2][j] = a[x2][j+1]
            mini = min(a[x2][j], mini)
        for j in range(x1, x2):
            a[j][y1] = a[j+1][y1]
            mini = min(a[j][y1], mini)
        for j in range(x2, x1, -1):
            a[j][y2] = a[j-1][y2]
            mini = min(a[j][y2], mini)
        a[x1+1][y2] = rightTop
        a[x2-1][y1] = leftBottom
        
        mini = min(mini, rightTop, leftBottom)
        
        answer.append(mini)
        
        
        
    return answer