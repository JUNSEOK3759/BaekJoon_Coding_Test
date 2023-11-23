def solution(want, number, discount):
    answer = 0
    a = {want[i] :  number[i] for i in range(len(want))}
    # a.sort(key = lambda x : (x[0]))
    k = len(discount)
    # print(a)
    # print()
    for i in range(k-9):
        x = {}
        for j in range(i, i+10):
            if discount[j] not in x:
                x[discount[j]] = 1
            else:
                x[discount[j]] += 1
        # print(x)
        if a == x:
            answer += 1
            
        
    
    return answer