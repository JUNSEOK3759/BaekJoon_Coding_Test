def solution(players, callings):
    player = {}
    rank = {}
    
    for i in range(len(players)):
        player[players[i]] = i+1
        rank[i+1] = players[i]
    
    for i in callings:
        currentIndex = player[i]
        player[i] = currentIndex-1
        player[rank[currentIndex-1]] = currentIndex
        
        rank[currentIndex] = rank[currentIndex-1]
        rank[currentIndex-1] = i
    return list(rank.values())