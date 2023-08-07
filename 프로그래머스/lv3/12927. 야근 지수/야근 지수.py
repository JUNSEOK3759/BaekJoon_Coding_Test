import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return 0
    x =[-i for i in works]
    heapq.heapify(x)
    
    while n:
        n-=1
        y = heapq.heappop(x)
        y += 1
        heapq.heappush(x, y)
    return sum([i**2 for i in x])