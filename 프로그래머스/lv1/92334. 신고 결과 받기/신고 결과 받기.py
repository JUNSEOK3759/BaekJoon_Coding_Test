# def solution(id_list, report, k):
    # answer = [0] * len(id_list)
    # a = {}
    # for i in set(report):
    #     x = i.split()
    #     if x[1] in a.keys():
    #         a[x[1]].add(x[0])
    #     else:
    #         a[x[1]] = {x[0]}
    # print(a)
    # lis = list()
    # for values in a.values():
    #     if len(values) >= k:
    #         lis.append(list(values))
    #         # for i in values:
    #         #     answer[id_list.index(i)] += 1
    # print(lis)
    # return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    declare = [0] * len(id_list)
    a = {}
    for i in set(report):
        x = i.split()
        if x[0] in a.keys():
            a[x[0]].add(x[1])
        else:
            a[x[0]] = {x[1]}
        declare[id_list.index(x[1])] += 1
    for i in range(len(declare)):
        if declare[i] >= k:
            for key, value in a.items():
                if id_list[i] in value:
                    answer[id_list.index(key)] += 1       
    return answer