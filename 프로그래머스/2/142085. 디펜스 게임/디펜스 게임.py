import heapq
def solution(n, k, enemy):
    answer = 0
    a = []
    tot = 0
    for i in enemy:
        tot += i
        heapq.heappush(a, -i)
        if tot > n:
            if k == 0:
                break
            k -= 1
            tot += heapq.heappop(a)
        answer += 1
    return answer

