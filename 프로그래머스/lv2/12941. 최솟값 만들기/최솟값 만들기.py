def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    while len(A) >0:
        answer += A[-1] * B[-1]
        A.pop(-1)
        B.pop(-1)
    return answer