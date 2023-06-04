def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()
    answer = []
    x = lottos.count(0)
    cnt = 0
    
    if x == 6:
        answer = [1, 6]
    elif lottos == win_nums:
        answer = [1, 1]
    else:
        for i in lottos:
            if i in win_nums:
                cnt += 1
        if cnt+x in [0, 1]:
            answer = [6, 6]
        else:
            answer.append(7-(cnt+x))
            if cnt == 0:
                answer.append(6)
            else:
                answer.append(7-cnt)
#     answer = []
    
#     a = [6, 6, 5, 4, 3, 2 ,1]
#     cnt=0
#     x = lottos.count(0)
#     for i in lottos:
#         if i in win_nums:
#             cnt += 1
#     answer = [a[cnt+x], a[cnt]]
    return answer