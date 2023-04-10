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
    print(x.index('A'),x.index('E'), x.index('I'), x.index('O'), x.index('U'))
    print(x)
    answer = x.index(word) + 1
    return answer