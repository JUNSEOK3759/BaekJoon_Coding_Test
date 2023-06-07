from collections import Counter
def solution(str1, str2):
    
    s1 = str1.lower()
    s2 = str2.lower()
    a, b = [], []
    for i in range(len(s1)-1):
        if s1[i].isalpha() and s1[i+1].isalpha():
            a.append(s1[i]+s1[i+1])
    for i in range(len(s2)-1):
        if s2[i].isalpha() and s2[i+1].isalpha():
            b.append(s2[i]+s2[i+1])
    x = Counter(a)
    y = Counter(b)
    
    inner = list((x & y).elements())
    union = list((x | y).elements())
    
    return 65536 if not inner and not union else int(len(inner) / len(union) * 65536)