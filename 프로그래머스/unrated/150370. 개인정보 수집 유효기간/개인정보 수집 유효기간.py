def solution(today, terms, privacies):
    answer = []
    
    def separate(n):
        a, b, c = n.split('.')
        k = (int(a) * 28 * 12) + (int(b) * 28) + int(c)
        return k
    
    def calendar(n):
        x, y = n.split()
        k = separate(x)
        return k, y
    
    tod = separate(today)
    
    a = {}
    for i in terms:
        x, y =i.split(' ')
        a[x] = int(y) * 28
    
    for i in range(len(privacies)):
        day, alp = calendar(privacies[i])
        day += a[alp]
        if tod >= day:
            answer.append(i+1)
    
    return answer