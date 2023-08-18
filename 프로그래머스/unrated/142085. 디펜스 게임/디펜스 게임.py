import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    total = 0
    
    for i in enemy:
        total += i
        heapq.heappush(heap, -i)
        if total > n:
            if k == 0:
                break
            k -= 1
            total += heapq.heappop(heap)
        answer += 1
    return answer