def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def dfs(x, y, n):
        temp = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if temp != arr[i][j]:
                    n //= 2
                    dfs(x, y, n)
                    dfs(x+n, y, n)
                    dfs(x, y+n, n)
                    dfs(x+n, y+n, n)
                    return
        answer[temp] += 1
    dfs(0, 0, n)
    return answer