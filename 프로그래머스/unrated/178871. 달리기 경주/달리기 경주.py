def solution(players, callings):
    player = {}
    rank = {}
    
    for i in range(len(players)):
        player[players[i]] = i+1
        rank[i+1] = players[i]
        
    for i in callings:
        current = player[i]
        player[i] = current-1
        player[rank[current-1]] = current
        rank[current] = rank[current-1]
        rank[current-1] = i
        
    return list(rank.values())