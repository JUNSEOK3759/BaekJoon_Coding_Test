def solution(today, terms, privacies):
    answer = []
    t1, t2, t3 = today.split(".")
    t = (int(t1)*336) + (int(t2) * 28) + int(t3)
    term = {}
    for i in terms:
        x, y = i.split(" ")
        term[x] = int(y) * 28
    for i in range(len(privacies)):
        x, y = privacies[i].split(' ')
        x1, x2, x3 = x.split('.')
        totX = (int(x1)*336) + (int(x2) * 28) + int(x3)
        if abs(totX - t) >= term[y]:
            answer.append(i+1)
    return answer