from collections import Counter
def solution(str1, str2):
    
    str1 , str2 = str1.lower(), str2.lower()
    a, b = [], []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i]+str2[i+1])
    a, b = Counter(a), Counter(b)
    print('a :', a)
    print('b :', b)
    x = list((a&b).elements())
    y = list((a|b).elements())
    print(f'x : {x}')
    print(f'y : {y}')
    return int(len(x) / len(y) * 65536) if x or y else 65536