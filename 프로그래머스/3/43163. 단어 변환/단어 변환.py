answer = 0
def dfs(l, s, target, words, n, ch):
    global answer
    if l == n:
        return 0
    if s == target:
        return
    else:
        for i in range(n):
            if difference(words[i], s) == 1 and ch[i] == 0:
                ch[i] = 1
                answer += 1
                dfs(l+1, words[i], target, words, n, ch)
                break
        else:
            return 0

def difference(x, y):
    dif = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            dif += 1
    return dif
    

def solution(begin, target, words):
    
    
    if target in words:
        words.remove(target)
        words.insert(0, target)
    else:
        return 0
    
    n = len(words)
    ch = [0 for _ in range(n)]
    
    dfs(0, begin,target,words,n,ch)
    
    
    return answer