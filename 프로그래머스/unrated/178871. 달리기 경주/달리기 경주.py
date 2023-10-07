def solution(players, callings):
    answer = []
    a = {players[i] : i for i in range(len(players))}
    b = {i : players[i] for i in range(len(players))}
    for i in callings:
        x = a[i]
        a[b[x]] = x-1
        a[b[x-1]] = x
        
        b[x] = b[x-1]
        b[x-1] = i
    
    for x in b.values():
        answer.append(x)
    return answer