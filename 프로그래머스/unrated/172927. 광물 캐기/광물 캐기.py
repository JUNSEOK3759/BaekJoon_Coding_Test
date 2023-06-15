def solution(picks, minerals):
    answer = 0
    diamondScore = {'diamond' : 1, 'iron' : 1, 'stone' : 1}
    ironScore = {'diamond' : 5, 'iron' : 1, 'stone' : 1}
    stoneScore = {'diamond' : 25, 'iron' : 5, 'stone' : 1}
    cnt = 0
    a = []
    for i in range(0, len(minerals), 5):
        if cnt == sum(picks):
            break
        y = minerals[i : i+5]
        x = y if y else minerals[i : ]
        a.append(x)
        cnt += 1
    a.sort(key = lambda x : (x.count('diamond'), x.count('iron'), x.count('stone')), reverse = True)
    
    for i in a:
        if picks[0] > 0:
            picks[0] -= 1
            for j in i:
                answer += diamondScore[j]
        elif picks[1] > 0:
            picks[1] -= 1
            for j in i:
                answer += ironScore[j]
        elif picks[2] > 0:
            picks[2] -= 1
            for j in i:
                answer += stoneScore[j]
    return answer