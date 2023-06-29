answer = 0
def solution(numbers, target):
    n = len(numbers)
    def dfs(l, summ):
        global answer
        if l == n:
            if summ == target:
                answer += 1
            return 
        else:
            dfs(l+1, summ + numbers[l])
            dfs(l+1, summ - numbers[l])
    dfs(0, 0)
    return answer