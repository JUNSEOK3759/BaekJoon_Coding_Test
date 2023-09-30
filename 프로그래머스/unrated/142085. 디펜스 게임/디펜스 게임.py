import heapq
def solution(n, k, enemy):
    answer = 0
    total = 0
    heap = []
    
    for e in enemy:
        total += e
        heapq.heappush(heap, -e)
        if total > n:
            if k == 0:
                break
            k -= 1
            total += heapq.heappop(heap)
        answer += 1

    return answer