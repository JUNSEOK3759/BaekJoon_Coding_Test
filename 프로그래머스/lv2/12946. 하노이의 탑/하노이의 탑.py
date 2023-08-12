def solution(n):
    answer = []
    def hanoi(start, end, mid, n):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start, mid, end, n-1)
            hanoi(start, end, mid, 1)
            hanoi(mid, end, start, n-1)
    hanoi(1, 3, 2, n)
    return answer