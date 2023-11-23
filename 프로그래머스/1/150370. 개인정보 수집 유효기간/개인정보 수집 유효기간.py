def solution(today, terms, privacies):
    answer = []
    t = {}
    for i in terms:
        x, y = i.split(' ')
        t[x] = int(y)
    year, month, day = today.split('.')
    tod = (int(year) * 28 * 12) + (int(month) * 28) + int(day)
    
    for i in range(len(privacies)):
        a, b = privacies[i].split(' ')
        y, m, d = a.split('.')
        tot = (int(y) * 28 * 12) + (int(m) * 28) + int(d)
        x = (int(t[b]) * 28)
        tot += x 
        if tod >= tot:
            
            answer.append(i+1)
    
    return answer