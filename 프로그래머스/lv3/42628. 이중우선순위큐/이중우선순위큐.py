import heapq
def solution(operations):
    answer = []
    
    heapq.heapify(answer)
    
    for i in operations:
        x, y = i.split(' ')
        y = int(y)
        
        if x == 'I':
            heapq.heappush(answer, y)
        else:
            if answer:
                if y == -1:
                    heapq.heappop(answer)
                else:
                    heapq._heapify_max(answer)
                    heapq._heappop_max(answer)
                    heapq.heapify(answer)
        
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]