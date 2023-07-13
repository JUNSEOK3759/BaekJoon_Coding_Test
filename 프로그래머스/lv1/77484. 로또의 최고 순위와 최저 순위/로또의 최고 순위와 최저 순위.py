def solution(lottos, win_nums):
    cnt = lottos.count(0)
    
    if cnt == len(win_nums):
        return [1, 6]
    res = 0
    
    for i in lottos:
        if i in win_nums:
            res += 1
            
    
    if res == 0 and cnt == 0:
        return [6, 6]
    else:
        return [7-res-cnt, 7-res]