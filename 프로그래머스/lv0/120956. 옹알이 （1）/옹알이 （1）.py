import itertools
def solution(babbling):
    cnt = 0
    a = ["aya", "ye", "woo", "ma"]
    x = []
    for i in range(1, 5):
        for j in itertools.permutations(a, i):
            x.append(''.join(j))
    for i in babbling:
        if i in x:
            cnt += 1
    return cnt