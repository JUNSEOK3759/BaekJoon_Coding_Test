def solution(today, terms, privacies):
    answer = []
    def calendar(n):
        x,  y = n.split()
        a, b, c = x.split('.')
        k = (int(a) * 28 * 12) + (int(b) * 28) + int(c)
        return k, y
    
    x, y, z = today.split('.')
    tod = (int(x)* 28 * 12) + (int(y) * 28) + int(z)
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