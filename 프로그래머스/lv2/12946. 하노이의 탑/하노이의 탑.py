def solution(n):
    answer = []
    def hanoi(start, end, middle, n):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start,middle,end, n-1)
            hanoi(start,end,middle, 1)
            hanoi(middle,end,start, n-1)
    hanoi(1, 3, 2, n)
    return answer