def solution(clothes):
    answer = 1
    a = {}
    for x,y in clothes:
        if y not in a:
            a[y] = [x]
        else:
            a[y].append(x)
    for i in a.values():
        answer *= len(i) + 1
    return answer - 1


def solution1(clothes):
    answer = 1
    a = {}
    for i in clothes:
        y, x = i
        if x not in a:
            a[x] = [y]
        else:
            a[x].append(y)

    for i in a.values():
        answer *= len(i) + 1
    return answer -1