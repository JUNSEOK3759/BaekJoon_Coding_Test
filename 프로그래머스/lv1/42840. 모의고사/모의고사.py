def solution(n):
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    res = [0 for _ in range(3)]
    for x, y in enumerate(n):
        if y == p[0][x % len(p[0])]:
            res[0] += 1
        if y == p[1][x % len(p[1])]:
            res[1] += 1

        if y == p[2][x % len(p[2])]:
            res[2] += 1
        ans = []
    for i, x in enumerate(res):
        if x == max(res):
            ans.append(i+1)
    
    
        
    return ans