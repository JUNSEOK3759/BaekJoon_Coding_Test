import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while scoville[0] < K and len(scoville) > 1:
        x, y = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, x + (y*2))
        answer += 1
    if max(scoville) < K:
        return -1
    return answer