from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    
    a = list((x&y).elements())
    a.sort(reverse = True)

    if a:
        if a[0] != '0':
            return ''.join(a)
        else:
            return '0'
    else:
        return '-1'