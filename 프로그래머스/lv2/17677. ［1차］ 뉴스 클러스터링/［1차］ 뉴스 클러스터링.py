from collections import Counter
import re
import math
def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    a, b = [], []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            a.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            b.append(str2[i] + str2[i+1])
            
    x = Counter(a)
    y = Counter(b)
    
    inner = list((x & y).elements())
    union = list((x | y).elements())
    
    return 65536 if not inner and not union else int(len(inner) / len(union) * 65536)