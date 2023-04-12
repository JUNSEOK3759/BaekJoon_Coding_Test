import heapq
from collections import deque
def solution(operations):
    heap = []
    heap1 = []
    heapq.heapify(heap)
    for i in operations:
        x, y = i.split(" ")
        if x == "I":
            y = int(y)
            heapq.heappush(heap, y)
        else:
            if heap:
                if y == "1":
                    heapq._heapify_max(heap)
                    heapq._heappop_max(heap)
                    heapq.heapify(heap)
                    
                else:
                    heapq.heappop(heap)
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]