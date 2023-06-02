def solution(players, callings):
    answer = []
    player = {}
    lank = {}
    
    for i in range(len(players)):
        player[players[i]] = i+1
        lank[i+1] = players[i]
        
    for i in callings:
        currentIndex = player[i]
        player[i] = currentIndex-1
        player[lank[currentIndex-1]] = currentIndex
        
        
        lank[currentIndex] = lank[currentIndex-1]
        lank[currentIndex-1] = i
        
    answer = list(lank.values())
    return answer