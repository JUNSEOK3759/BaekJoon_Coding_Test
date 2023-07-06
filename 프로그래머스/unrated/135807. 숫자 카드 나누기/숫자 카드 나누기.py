import math
def solution(arrayA, arrayB):
    answer = 0
    a = arrayA[0]
    b = arrayB[0]
    for i in arrayA:
        a = math.gcd(a, i)
    
    for i in arrayB:
        b = math.gcd(b, i)
    
    for i in arrayA:
        if i % b == 0:
            break
    else:
         answer = max(answer, b)
    
    for i in arrayB:
        if i % a == 0:
            break
    else:
         answer = max(answer, a)   
    
    return answer