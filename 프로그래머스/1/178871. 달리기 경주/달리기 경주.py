def solution(players, callings):
    answer = []
    x = len(players)
    a = {players[i] : i+1 for i in range(x)}
    b = {i+1 : players[i] for i in range(x)}
    
    for call in callings:
        q = a[call]
        a[call] -= 1
        
        w = b[q-1]
        b[q-1] = call
        a[w] = q
        
        b[q] = w

    
    return [i for i in b.values()]