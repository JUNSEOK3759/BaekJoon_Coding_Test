import itertools
import re
def solution(babbling):
    cnt = 0
    a = ["aya", "ye", "woo", "ma"]
    for i in a:
        x = []
        for j in range(len(babbling)):
            if i*2 in babbling[j]:
                x.append(babbling[j])
        for j in x:
            babbling.remove(j)
    
    for i in range(len(babbling)):
        cnt = 0
        while cnt < len(a):
            if a[cnt] in babbling[i]:
                babbling[i] = re.sub(a[cnt], 'X', babbling[i])
            else:
                cnt += 1
    
    for i in range(len(babbling)):
        babbling[i] = re.sub('X','', babbling[i])
    return babbling.count('') 