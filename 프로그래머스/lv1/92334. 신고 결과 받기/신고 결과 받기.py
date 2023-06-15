def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    a = {}
    for i in report:
        x, y = i.split(' ')
        if y in a:
            a[y].add(x)
        else:
            a[y] = {x}
    for x, y in a.items():
        if len(y) >= k:
            for i in y:
                answer[id_list.index(i)] += 1
    return answer