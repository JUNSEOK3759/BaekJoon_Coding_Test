def solution(players, callings):
    answer = []
    player = {players[i] : i for i in range(len(players))}
    rank = {i : players[i]  for i in range(len(players))}
    for i in callings:
        x = player[i]
        player[i] = x-1
        player[rank[x-1]] = x
         
        rank[x] = rank[x-1]
        rank[x-1] = i
    
    for i in rank.values():
        answer.append(i)
    return answer