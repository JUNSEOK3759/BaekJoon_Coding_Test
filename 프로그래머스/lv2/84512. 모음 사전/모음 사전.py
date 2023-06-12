import itertools
def solution(word):
    answer = 0
    x = ['A', 'E', 'I', 'O', 'U']
    a = sorted(x * 5)
    k = set()
    for i in range(1, 6):
        for j in itertools.permutations(a, i):
            k.add(''.join(j))
    k = sorted(k)
    return k.index(word)+1