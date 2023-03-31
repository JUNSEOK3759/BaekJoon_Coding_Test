def solution(order):
    temp = []
    i = 1
    now = 0
    while i != len(order)+1:
        temp.append(i)
        while temp[-1] == order[now]:
            now += 1
            temp.pop()
            if len(temp) == 0:
                break
        i += 1
    return now