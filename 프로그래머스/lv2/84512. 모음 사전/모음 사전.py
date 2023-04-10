import itertools
def solution(word):
    answer = 0
    a = ['A', 'E', 'I', 'O', 'U'] *5
    x = []
    
    for i in range(1, 6):
        for j in list(itertools.combinations(a, i)):
            x.append(''.join(j))
    x = list(set(x))
    x.sort()
    answer = x.index(word) + 1
    return answer