def solution(keymap, targets):
    answer = []
    
    for i in targets:
        res = 0
        for j in i:
            mini = 2147000000
            for k in keymap:
                k = list(k)
                if j in k:
                    mini = min(k.index(j)+1, mini)
            res += mini
        if res >= 2147000000:
            res = -1
        answer.append(res)
    return answer