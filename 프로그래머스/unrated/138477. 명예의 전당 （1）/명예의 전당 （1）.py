import heapq
def solution2 (k, score):
    answer = []
    x = []
    for i in score:
        if len(x) < k:
            x.append(i)
            x.sort(reverse = True)
            answer.append(min(x))
            
        elif len(x) == k:
            if i < min(x):     
                answer.append(min(x))
            else:
                x[-1] = i
                answer.append(min(x))
                x.sort(reverse = True)
    return answer

def solution(k, score):
    answer = []
    x = []
    heapq.heapify(x)
    for i in score:
        if len(x) < k:
            heapq.heappush(x, i)
            answer.append(min(x))
        elif len(x) == k:
            if i > min(x):
                heapq.heappop(x)
                heapq.heappush(x, i)
            answer.append(min(x))
            
    return answer
    