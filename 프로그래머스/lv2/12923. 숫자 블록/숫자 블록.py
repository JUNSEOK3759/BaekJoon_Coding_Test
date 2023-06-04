import math
def solution(begin, end):
    MAX = 10000000
    def isValue(i):
        k = 1
        for x in range(2, int(math.sqrt(i))+1):
            if i % x == 0:
                k = x
                if i // x <= MAX:
                    return  i // x
        else:
            return k
    answer = []
    
    for i in range(begin, end + 1):
        if i > 1:
            x = isValue(i)
            answer.append(x)
        else:
            answer.append(0)
    return answer