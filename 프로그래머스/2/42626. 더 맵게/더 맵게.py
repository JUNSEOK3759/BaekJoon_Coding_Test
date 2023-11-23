import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            answer += 1
            x = heapq.heappop(scoville)
            y = heapq.heappop(scoville)
            heapq.heappush(scoville, x + (y*2))
        except IndexError:
            return -1
    return answer