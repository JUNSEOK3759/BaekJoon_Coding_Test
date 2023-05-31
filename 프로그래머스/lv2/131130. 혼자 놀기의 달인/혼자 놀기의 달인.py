def solution(cards):
    answer = 1
    a = {}
    ch = [0 for _ in range(len(cards)+1)]
    for i in range(len(cards)):
        a[i+1] = cards[i]
    print(a)
    x = 1
    asd = []
    for x, y in a.items():
        qwe = []
        while ch[x] != 1:
            qwe.append(a[x])
            ch[x] = 1
            x = a[x]
        qwe.sort()
        if qwe not in asd:
            asd.append(qwe)
    
    asd.sort(key = lambda x : (len(x)), reverse = True)
    for i in range(2):
        answer *= len(asd[i])
    
    return answer