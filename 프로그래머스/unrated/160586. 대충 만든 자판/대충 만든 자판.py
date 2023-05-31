def solution(keymap, targets):
    answer = []
    for i in targets:
        res = 0
        for j in i:
            cnt = 2147483647
            for k in range(len(keymap)):
                for l in range(len(keymap[k])):
                    if j == keymap[k][l]:
                        if l+1 < cnt:
                            cnt = l+1
                        break
    
            res += cnt 
        answer.append(res if res < 2147483647 else -1)
                        
    return answer 