import math
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        div = i // n
        mod = i % n
        x = max(div, mod)
        answer.append(x+1)
    return answer