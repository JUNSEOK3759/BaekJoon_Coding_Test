import re
def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    b = [0, 0, 0, 0]
    for i in a:
        x = []
        for j in babbling:
            if i*2 in j:
                x.append(j)
        for j in x:
            babbling.remove(j)
    for i in range(len(babbling)):
        cnt = 0
        while cnt < len(a):
            if a[cnt] in babbling[i]:
                babbling[i] = re.sub(a[cnt], 'X', babbling[i])
            else:
                cnt += 1
        babbling[i] = re.sub('X', '', babbling[i])
    return babbling.count('')