import itertools
def solution(skill, skill_trees):
    answer = 0
    
    skill_list = list(skill)
    for i in skill_trees:
        a = {}
        for j in range(len(i)):
            x = i[j]
            if x in skill_list:
                a[j] = x
        x = ''.join([i for i in a.values()])
        if x == skill[:len(x)]:
            answer += 1
    return answer