def solution(prices):
    answer = []
    x = len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(x - i-1)
                
    return answer